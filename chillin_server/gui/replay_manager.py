# -*- coding: utf-8 -*-

# python imports
import os
import struct
from datetime import datetime

# project imports
from ..config import Config
from .parser import Parser


class ReplayManager:

    REPLAY_FILE_EXTENSION = 'cr'

    def __init__(self):
        self._save_replay = Config.config['gui']['save_replay']
        if self._save_replay:
            self._parser = Parser()
            self._replay_path = self._make_replay_path()
            self._prepare_replay_file()


    def _make_replay_path(self):
        replay_dir = Config.config['gui'].get('replay_dir') or '.'
        replay_filename = Config.config['gui'].get('replay_filename') or \
                datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        if not os.path.exists(replay_dir):
            os.makedirs(replay_dir)
        return os.path.join(
            replay_dir,
            "%s.%s" % (replay_filename, self.REPLAY_FILE_EXTENSION)
        )


    def _prepare_replay_file(self):
        if os.path.exists(self._replay_path):
            os.remove(self._replay_path)


    def store_message(self, msg):
        if not self._save_replay:
            return

        msg_data = self._parser.encode(msg)
        size = struct.pack('I', len(msg_data))
        with open(self._replay_path, 'ab') as file:
            file.write(size + msg_data)
