# -*- coding: utf-8 -*-

# circuits imports
from circuits import Event


class start_game(Event):

	def __init__(self):
		super(start_game, self).__init__()


class end_game(Event):

    def __init__(self, winner_sidename, details):
        super(end_game, self).__init__(winner_sidename=winner_sidename, details=details)


class process_cycle(Event):

	def __init__(self):
		super(process_cycle, self).__init__()
