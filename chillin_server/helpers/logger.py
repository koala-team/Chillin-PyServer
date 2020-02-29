# -*- coding: utf-8 -*-

# python imports
import os
import json
from datetime import datetime

# project imports
from ..config import Config


def log(text):
    print(text)


def log_file(new_json_data):
    path = _make_log_path()
    json_data = {}
    if os.path.exists(path):
        with open(path) as f:
            json_data.update(json.loads(f.read()))
    json_data.update(new_json_data)
    with open(path, 'w') as f:
        f.write(json.dumps(json_data, indent=4) + '\n')


_start_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
def _make_log_path():
    log_dir = Config.config['general'].get('log_dir', '.')
    log_filename = Config.config['general'].get('log_filename', _start_time)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    return os.path.join(log_dir, "%s.json" % log_filename)
