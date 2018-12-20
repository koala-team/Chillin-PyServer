# -*- coding: utf-8 -*-

# project imports
from ..config import Config
from .parser import Parser
from .messages import SceneActions
from .scene_actions import StoreBundleData


class Scene:

    def __init__(self, replay, send_queue):
        self._send_queue = send_queue
        self._replay = replay

        self._current_ref = 0
        self._ref_table = {}
        self._reset_actions()


    def _reset_actions(self):
        self._actions = SceneActions([], [])


    def _get_ref(self, ref):
        ref_type = type(ref)
        if ref_type == str:
            return self._ref_table[ref]
        if ref_type == int:
            return ref
        raise TypeError("an integer or string is required")


    def _del_ref(self, ref):
        ref_type = type(ref)
        if ref_type == str:
            del self._ref_table[ref]
            return
        if ref_type == int:
            return
        raise TypeError("an integer or string is required")


    def initialize(self):
        self._store_all_bundles_data()
        self.apply_actions()


    def apply_actions(self):
        self._send_queue.put(self._actions)
        self._replay.store_message(self._actions)
        self._reset_actions()


    def add_action(self, action):
        act_type, act_payload = Parser.get_tuplestring(action)
        self._actions.action_types.append(act_type)
        self._actions.action_payloads.append(act_payload)


    # Actions

    def _store_all_bundles_data(self):
        if not Config.config['gui']['auto_sync_bundles']:
            return
        for name, path in Config.config['gui']['bundles'].items():
            with open(path, 'rb') as f:
                data = Parser.get_string(f.read())
                self.add_action(StoreBundleData(bundle_name=name, bundle_data=data))
