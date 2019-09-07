# -*- coding: utf-8 -*-

# project imports
from ..config import Config
from .parser import Parser
from .messages import SceneActions
from .reference_manager import ReferenceManager


class Scene:

    def __init__(self, replay, send_queue):
        self._replay = replay
        self._send_queue = send_queue
        self._reset_actions()

        self.rm = ReferenceManager()


    def _reset_actions(self):
        self._actions = SceneActions([], [])


    def initialize(self):
        self.apply_actions()


    def apply_actions(self):
        self._send_queue.put(self._actions)
        self._replay.store_message(self._actions)
        self._reset_actions()


    def add_action(self, action):
        act_type, act_payload = Parser.get_tuplestring(action)
        self._actions.action_types.append(act_type)
        self._actions.action_payloads.append(act_payload)

