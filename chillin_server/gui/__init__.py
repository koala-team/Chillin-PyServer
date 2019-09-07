# -*- coding: utf-8 -*-

# project imports
from .tools import GuiTools
from .protocol import Protocol
from .screen import Screen
from ..helpers.master_server import authenticate_spectator


class GUI:

    def __init__(self):
        GuiTools.initialize()
        self._protocol = Protocol(authenticate_spectator, Screen.game_info())
        self.screen = Screen(self._protocol.send_queue)


    def start(self):
        self._protocol.start()


    def stop(self):
        self._protocol.stop()
