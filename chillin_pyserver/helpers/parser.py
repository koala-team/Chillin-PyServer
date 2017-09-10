# -*- coding: utf-8 -*-

# python imports
import sys
import os
import imp
import inspect
from enum import Enum

# project imports
from . import messages

PY3 = sys.version_info > (3,)


class Parser:

    def __init__(self, ks_command_files):
        self._message_factory = MessageFactory(ks_command_files)


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
        msg = res

        cmd_type = None
        cmd = None
        if isinstance(msg, messages.BaseCommand):
            cmd_type = msg.type
            cmd = mf.get_command(msg.type)
            cmd.deserialize(self.get_bytes(msg.payload))

        return msg_type, msg, cmd_type, cmd


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

    def __init__(self, ks_command_files):
        self._installed_messages = self._load_messages()
        self._installed_commands = self._load_commands(ks_command_files)


    def _load_messages(self):
        module = messages
        return self._load_ks_objects([module])


    def _load_commands(self, files):
        modules = []
        for file in files:
            file = os.path.splitext(file)[0] + '.py'
            name = os.path.splitext(os.path.basename(file))[0]
            module = imp.load_source(name, file)
            modules.append(module)
        return self._load_ks_objects(modules)


    def _load_ks_objects(self, modules):
        objects = {}

        for module in modules:
            for _, member in inspect.getmembers(module, inspect.isclass):
                if not issubclass(member, Enum):
                    objects[member.name()] = member

        return objects


    def get_message(self, message_name):
        return self._installed_messages[message_name]()


    def get_command(self, command_name):
        return self._installed_commands[command_name]()
