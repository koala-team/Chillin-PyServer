# -*- coding: utf-8 -*-

# circuits imports
from circuits import handler, Component

# project imports
from ..config import Config
from ..events.network import stop_accepting, stop_receiving
from ..events.protocol import send_msg
from ..events.core import cmd_received, all_agents_joined, broadcast_msg

from ..helpers.logger import log
from ..helpers.auth import AgentAuthenticator
from ..helpers.master_server import get_token_info, send_match_result
from ..helpers.messages import JoinOfflineGame, JoinOnlineGame, ClientJoined, \
        AgentJoined, AgentLeft, BaseCommand


class Core(Component):

    def __init__(self, screen):
        super(Core, self).__init__()

        self._game_ended = False
        self._screen = screen

        self._offline_mode = Config.config['general']['offline_mode']
        self._agent_authenticator = AgentAuthenticator(
            Config.config['sides'],
            Config.config['general']['allowed_teams']
        )
        self._match_id = None if self._offline_mode else Config.config['general']['match_id']


    @handler('msg_received')
    def on_msg_recv(self, sock, msg_type, msg, cmd_type, cmd):
        if self._agent_authenticator.is_joined(sock):
            if isinstance(msg, BaseCommand):
                self._handle_command(sock, msg, cmd_type, cmd)
            else:
                self._handle_control_message(sock, msg_type, msg)

        elif msg_type in [JoinOfflineGame.name(), JoinOnlineGame.name()]:
            side_name, team_nickname = self._handle_join_message(sock, msg_type, msg)
            joined = True if side_name else False

            # send response to requesting client
            client_joined_msg = ClientJoined(
                joined = joined,
                side_name = side_name,
                sides = Config.config['sides']
            )
            self.fire(send_msg(sock, client_joined_msg))

            # notify all clients when a new agent joins
            if joined:
                agent_joined_msg = AgentJoined(
                    side_name = side_name,
                    agent_name = msg.agent_name,
                    team_nickname = team_nickname
                )
                self.fire(broadcast_msg(agent_joined_msg))
                self._screen.display_agent_joined(
                    agent_joined_msg.side_name,
                    agent_joined_msg.agent_name,
                    agent_joined_msg.team_nickname
                )
                log("Agent %s-%s has joined -> team_nickname: %s" % (
                    agent_joined_msg.side_name, agent_joined_msg.agent_name, agent_joined_msg.team_nickname
                ))

            # notify other components when all agents have joined
            if self._agent_authenticator.all_joined():
                self.fire(all_agents_joined())
                self.fire(stop_accepting())
                log("All agents have joined")


    @handler('broadcast_msg')
    def on_broadcast_msg(self, msg, side_name=None, agent_name=None):
        kwargs = {}
        if side_name is not None:
            kwargs.update(side_name=side_name)
            if agent_name is not None:
                kwargs.update(agent_name=agent_name)

        for agent_info in self._agent_authenticator.get_info(**kwargs):
            self.fire(send_msg(agent_info['sock'], msg))


    @handler('client_disconnected')
    def on_disconnected(self, sock):
        if self._game_ended:
            return

        agent_info = self._agent_authenticator.get_info(sock=sock)
        if agent_info:
            agent_info = agent_info[0]
            agent_left_msg = AgentLeft(
                side_name = agent_info['side_name'],
                agent_name = agent_info['agent_name']
            )
            self.fire(broadcast_msg(agent_left_msg))
            self._screen.display_agent_left(
                agent_left_msg.side_name,
                agent_left_msg.agent_name
            )
            log("Agent %s-%s has left the game" % (agent_left_msg.side_name, agent_left_msg.agent_name))


    @handler('end_game')
    def on_end_game(self, winner_sidename, details):
        self._game_ended = True
        self.fire(stop_receiving())
        if not self._offline_mode:
            send_match_result(self._match_id, winner_sidename, details)
        self.parent.shutdown()


    def _handle_join_message(self, sock, msg_type, msg):
        side_name = ''
        team_nickname = ''

        if msg_type == JoinOfflineGame.name() and self._offline_mode:
            team_nickname = msg.team_nickname
            side_name = self._agent_authenticator.join(
                sock,
                msg.team_nickname,
                None,
                msg.agent_name
            )

        elif msg_type == JoinOnlineGame.name() and not self._offline_mode:
            client_team_id, client_agent_id, team_nickname = get_token_info(msg.token)
            side_name = self._agent_authenticator.join(
                sock,
                client_team_id,
                client_agent_id,
                msg.agent_name
            )

        return side_name, team_nickname


    def _handle_control_message(self, sock, msg_type, msg):
        # this is a control message and is not supported
        # may be supported later
        return


    def _handle_command(self, sock, msg, cmd_type, cmd):
        agent_info = self._agent_authenticator.get_info(sock=sock)[0]
        self.fire(
            cmd_received(
                agent_info['side_name'],
                agent_info['agent_name'],
                msg,
                cmd_type,
                cmd
            )
        )
