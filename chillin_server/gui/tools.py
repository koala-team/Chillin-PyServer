# -*- coding: utf-8 -*-

# project imports
from ..config import Config
from ..helpers.singleton import Singleton


class GuiTools(Singleton):

    @classmethod
    def initialize(cls):
        pass


    @classmethod
    def cycle_to_time(cls, cycle):
        return float(cycle) * Config.config['gui']['cycle_duration']


    @classmethod
    def time_to_cycle(cls, time):
        return float(time) / Config.config['gui']['cycle_duration']
