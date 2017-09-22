#! /usr/bin/env python
# -*- coding: utf-8 -*-

# python imports
import sys

# chillin imports
from chillin_server import GameServer, Config

# project imports
from game_handler import GameHandler


app = GameServer(sys.argv[1])
app.register_game_handler(GameHandler(Config.config))
app.run()
