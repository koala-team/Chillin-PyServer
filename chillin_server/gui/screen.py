# -*- coding: utf-8 -*-

# python imports
import sys

# project imports
from ..config import Config
from .messages import GameInfo
from .scene import Scene
from .messages import AgentJoined, AgentLeft, StartGame, EndGame
from .replay_manager import ReplayManager


class Screen:

    def __init__(self, send_queue):
        self._send_queue = send_queue
        self._replay_manager = ReplayManager()
        self.scene = Scene(self._replay_manager, send_queue)
        self._replay_manager.store_message(self.game_info())


    @staticmethod
    def game_info():
        return GameInfo(
            game_name = Config.config['general']['game_name'],
            sides = Config.config['sides'],
            gui_cycle_duration = Config.config['gui']['cycle_duration'],
            gui_side_colors = Config.config['gui']['side_colors']
        )


    def display(self, msg):
        self._send_queue.put(msg)
        self._replay_manager.store_message(msg)


    def display_agent_joined(self, side_name, agent_name, team_nickname):
        self.display(
            AgentJoined(
                side_name = side_name,
                agent_name = agent_name,
                team_nickname = team_nickname
            )
        )


    def display_agent_left(self, side_name, agent_name):
        self.display(
            AgentLeft(
                side_name = side_name,
                agent_name = agent_name
            )
        )


    def display_start_game(self, start_time):
        self.display(
            StartGame(
                start_time = start_time
            )
        )


    def display_end_game(self, winner_sidename, details):
        self.display(
            EndGame(
                winner_sidename = winner_sidename,
                details = details
            )
        )
