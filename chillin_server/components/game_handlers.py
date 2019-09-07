# -*- coding: utf-8 -*-

# python imports
from time import time
from threading import Thread, Timer

# circuits imports
from circuits import Component, handler

# project imports
from ..events.core import broadcast_msg
from ..events.game_handlers import start_game, end_game, process_cycle
from ..helpers.logger import log
from ..helpers.parser import Parser
from ..helpers.messages import StartGame, EndGame, BaseSnapshot, RealtimeSnapshot, TurnbasedSnapshot
from ..helpers.datetiming import utcnowts, strutcts
from ..gui.scene import Scene


class BaseGameHandler(Component):

    def __init__(self, config):
        super(BaseGameHandler, self).__init__()
        self._configure(config)

        self._accept_commands = False
        self._command_processor_threads = []
        self._screen = None
        self.game_running = False
        self.scene = Scene(None, None) # initialize is not necessary, just for auto completion


    def _configure(self, config):
        self.config = config['game_handler']
        self.sides = config['sides']


    def set_screen(self, screen):
        self._screen = screen
        self.scene = screen.scene


    @handler('cmd_received')
    def _on_cmd_recv(self, side_name, agent_name, msg, command_type, command):
        if self._accept_commands:
            t = Thread(
                target = self.on_recv_command,
                args = (side_name, agent_name, command_type, command)
            )
            self._command_processor_threads.append(t)
            t.start()


    def _wait_for_proccessing_commands(self):
        for t in self._command_processor_threads:
            t.join()
        self._command_processor_threads = []


    @handler('all_agents_joined')
    def _on_all_agents_joined(self):
        self.scene.initialize()
        self.on_initialize()
        self.on_initialize_gui()

        if self.config.get('start_time'):
            start_time = max(strutcts(self.config['start_time'], "%Y-%m-%d %H:%M"), utcnowts())
        else:
            start_time = utcnowts()
        start_time = int(start_time + 1) + self.config['start_waiting_time']
        msg = StartGame(start_time=start_time)
        self.fire(broadcast_msg(msg))
        self._screen.display_start_game(start_time=msg.start_time)

        t = Timer(
            start_time - utcnowts(),
            lambda : self.fire(start_game())
        )
        t.setDaemon(True)
        t.start()


    @handler('start_game')
    def _on_start_game(self):
        self._accept_commands = True
        self.game_running = True
        self.on_update_clients()
        log("Start the game")


    @handler('end_game')
    def _on_end_game(self, winner_sidename, details):
        msg = EndGame(
            winner_sidename = winner_sidename,
            details = details
        )
        self.fire(broadcast_msg(msg))
        self._screen.display_end_game(
            winner_sidename = msg.winner_sidename,
            details = msg.details
        )

        winner = winner_sidename or 'draw'
        log("Winner side: %s" % winner)
        if details:
            log("Details:")
            for name, sides in details.items():
                log("  %s:" % name)
                for side, val in sides.items():
                    log("    %s -> %s" % (side, val))



    def _send_snapshot(self, world, side_name=None, agent_name=None, msg=None):
        if not msg:
            msg = BaseSnapshot()
        _, msg.world_payload = Parser.get_tuplestring(world)
        self.fire(broadcast_msg(msg, side_name, agent_name))


    def send_snapshot(self, world, side_name=None, agent_name=None):
        self._send_snapshot(world, side_name, agent_name)


    @handler(False)
    def end_game(self, winner_sidename='', details={}):
        # null winner_sidename indicates a draw
        self.game_running = False
        self.fire(end_game(winner_sidename, details))


    # async
    def on_recv_command(self, side_name, agent_name, command_type, command):
        pass


    # sync
    def on_initialize(self):
        pass


    # sync
    def on_initialize_gui(self):
        pass


    # sync
    def on_update_clients(self):
        pass


    # sync
    def on_update_gui(self):
        pass



class RealtimeGameHandler(BaseGameHandler):

    def __init__(self, config):
        super(RealtimeGameHandler, self).__init__(config)
        self.current_cycle = 0
        self.cycle_duration = self.config['cycle_duration']

        self._change_cycle_timer = None
        self._command_counter = self._create_command_counter()


    def _create_command_counter(self):
        command_counter = {'total': 0, 'sides': {}}
        for side_name in self.sides:
            data = {'total': 0, 'agents': {}}
            for agent_name in self.sides[side_name]:
                data['agents'][agent_name] = 0
            command_counter['sides'][side_name] = data
        return command_counter


    def _reset_command_counter(self):
        self._command_counter['total'] = 0
        counter = self._command_counter['sides']
        for side_name in counter:
            counter[side_name]['total'] = 0
            for agent_name in counter[side_name]['agents']:
                counter[side_name]['agents'][agent_name] = 0


    @handler('cmd_received')
    def _on_cmd_recv(self, side_name, agent_name, msg, command_type, command):
        counter = self._command_counter
        if msg.cycle == self.current_cycle and \
                counter['sides'][side_name]['total'] < self.config['max_team_commands'] and \
                counter['sides'][side_name]['agents'][agent_name] < self.config['max_agent_commands']:

            counter['total'] += 1
            counter['sides'][side_name]['total'] += 1
            counter['sides'][side_name]['agents'][agent_name] += 1
            super(RealtimeGameHandler, self)._on_cmd_recv(
                    side_name, agent_name, msg, command_type, command)

            if counter['total'] == self.config['max_total_commands']:
                self._change_cycle(False)


    @handler('start_game')
    def _on_start_game(self):
        super(RealtimeGameHandler, self)._on_start_game()
        self._change_cycle()


    def _change_cycle(self, delayed=True):
        if delayed:
            t = Timer(
                self.cycle_duration,
                lambda: self.fire(process_cycle())
            )
            t.start()
            self._change_cycle_timer = t
        else:
            if self._change_cycle_timer:
                self._change_cycle_timer.cancel()
            self.fire(process_cycle())


    @handler('process_cycle')
    def _on_process_cycle(self):
        self._on_pre_process_cycle()
        self.on_process_cycle()
        self._on_post_process_cycle()
        self.on_update_gui()
        self.on_update_clients()
        if self.game_running:
            self._change_cycle()


    def _on_pre_process_cycle(self):
        self._accept_commands = False
        self._wait_for_proccessing_commands()


    def _on_post_process_cycle(self):
        self._reset_command_counter()
        self.current_cycle += 1
        self._accept_commands = True


    def _send_snapshot(self, world, side_name=None, agent_name=None, msg=None):
        if not msg:
            msg = RealtimeSnapshot()
        msg.current_cycle = self.current_cycle
        msg.cycle_duration = self.cycle_duration
        super(RealtimeGameHandler, self)._send_snapshot(world, side_name, agent_name, msg=msg)


    # sync
    def on_process_cycle(self):
        pass



class TurnbasedGameHandler(RealtimeGameHandler):

    def __init__(self, config):
        super(TurnbasedGameHandler, self).__init__(config)
        if self.config['auto_change_turn']:
            self.turn_allowed_sides = [self.config['auto_change_turn_sequence'][0]]
        else:
            self.turn_allowed_sides = []


    def set_turn_allowed_sides(self, sides):
        if not self.config['auto_change_turn']:
            self.turn_allowed_sides = sides


    @handler('cmd_received')
    def _on_cmd_recv(self, side_name, agent_name, msg, command_type, command):
        if side_name in self.turn_allowed_sides:
            super(TurnbasedGameHandler, self)._on_cmd_recv(
                    side_name, agent_name, msg, command_type, command)


    def _on_post_process_cycle(self):
        if self.config['auto_change_turn']:
            seq_num = (self.current_cycle + 1) % len(self.config['auto_change_turn_sequence'])
            self.turn_allowed_sides = [self.config['auto_change_turn_sequence'][seq_num]]

        super(TurnbasedGameHandler, self)._on_post_process_cycle()


    def _send_snapshot(self, world, side_name=None, agent_name=None, msg=None):
        if not msg:
            msg = TurnbasedSnapshot()
        msg.turn_allowed_sides = self.turn_allowed_sides
        super(TurnbasedGameHandler, self)._send_snapshot(world, side_name, agent_name, msg)
