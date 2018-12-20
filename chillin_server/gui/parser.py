# -*- coding: utf-8 -*-

# python imports
import sys
import os
import imp
import inspect
from enum import Enum

# project imports
from . import messages, scene_actions

PY3 = sys.version_info > (3,)


class Parser:

    def __init__(self):
        self._message_factory = MessageFactory()


    def encode(self, payload_obj):
        msg = messages.Message()
        msg.type, msg.payload = self.get_tuplestring(payload_obj)
        return msg.serialize()


    def decode(self, data):
        mf = self._message_factory

        msg = messages.Message()
        msg.deserialize(data)
        res = mf.get_message(msg.type)
        res.deserialize(self.get_bytes(msg.payload))

        msg_type = msg.type

        if msg_type == messages.SceneActions.name():
            msg = res
            res = []
            for i in range(len(msg.action_types)):
                act_type = msg.action_types[i]
                action = mf.get_message(act_type)
                action.deserialize(self.get_bytes(msg.action_payloads[i]))

                if act_type in ['CreateElement', 'EditElement']:
                    element = mf.get_message(action.element_type)
                    element.deserialize(self.get_bytes(action.element_payload))
                    res.append((act_type, element))
                else:
                    res.append(action)

        return msg_type, res


    @classmethod
    def get_tuplestring(cls, serializable_obj):
        return serializable_obj.name(), cls.get_string(serializable_obj.serialize())


    @staticmethod
    def get_string(bytes):
        return bytes.decode('ISO-8859-1') if PY3 else bytes


    @staticmethod
    def get_bytes(string):
        return string.encode('ISO-8859-1') if PY3 else string



class MessageFactory:

    def __init__(self):
        self._installed_messages = self._load_ks_objects([
            messages,
            scene_actions
        ])


    def _load_ks_objects(self, modules):
        objects = {}

        for module in modules:
            for _, member in inspect.getmembers(module, inspect.isclass):
                if not issubclass(member, Enum):
                    objects[member.name()] = member

        return objects


    def get_message(self, message_name):
        return self._installed_messages[message_name]()
