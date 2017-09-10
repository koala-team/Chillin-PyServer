# -*- coding: utf-8 -*-

# python imports
from time import sleep
from threading import Timer

# circuits imports
from circuits import Component, Event, handler

# project imports
from .config import Config
from .components.network import Network
from .components.protocol import Protocol
from .components.core import Core
from .gui import GUI

from .components.game_handlers import BaseGameHandler, RealtimeGameHandler, TurnbasedGameHandler


class shutdown(Event):

    def __init__(self):
        super(shutdown, self).__init__()



class GameServer(Component):

    def __init__(self, gamecfg_path):
        super(GameServer, self).__init__()

        Config.initialize(gamecfg_path)
        self._register_components()


    def _register_components(self):
        self._gui = GUI()
        self._network = Network().register(self)
        self._protocol = Protocol().register(self)
        self._core = Core(self._gui.screen).register(self)


    def register_game_handler(self, game_handler):
        game_handler.set_screen(self._gui.screen)
        self._game_handler = game_handler.register(self)


    def started(self, _):
        self._gui.start()


    def stop(self, *args, **kwargs):
        super(GameServer, self).stop(*args, **kwargs)
        self._gui.stop()


    @handler(False)
    def shutdown(self, max_wait=5):
        Timer(
            .5,
            lambda: self._shutdown(max_wait)
        ).start()


    def _shutdown(self, max_wait):
        if self._network.busy() and max_wait:
            self.shutdown(max_wait - 1)
        else:
            self.fire(shutdown())


    @handler('shutdown')
    def _on_shutdown(self):
        self.stop()
