# -*- coding: utf-8 -*-

# python imports
import json

# project imports
from .helpers.parser import PY3
from .helpers.singleton import Singleton


class Config(Singleton):

    @classmethod
    def initialize(cls, cfg_path):
        with open(cfg_path) as f:
            cls.config = cls._parse(f.read())


    @classmethod
    def _parse(cls, json_text):
        if PY3:
            return json.loads(json_text)
        return json_loads_byteified(json_text)



def json_loads_byteified(json_text):
    return _byteify(
        json.loads(json_text, object_hook=_byteify),
        ignore_dicts = True
    )


def _byteify(data, ignore_dicts=False):
    # if this is a unicode string, return its string representation
    if isinstance(data, unicode):
        return data.encode('utf-8')

    # if this is a list of values, return list of byteified values
    if isinstance(data, list):
        return [ _byteify(item, ignore_dicts=True) for item in data ]

    # if this is a dictionary, return dictionary of byteified keys and values
    # but only if we haven't already byteified it
    if isinstance(data, dict) and not ignore_dicts:
        return {
            _byteify(key, ignore_dicts=True): _byteify(value, ignore_dicts=True)
            for key, value in data.iteritems()
        }

    # if it's anything else, return it in its original form
    return data
