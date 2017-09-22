# -*- coding: utf-8 -*-

# circuits imports
from circuits import handler, Component

# project imports
from ..config import Config
from ..events.network import send_data
from ..events.protocol import msg_received
from ..helpers.parser import Parser


class Protocol(Component):

    def __init__(self):
        super(Protocol, self).__init__()

        self._parser = Parser(Config.config['general']['command_files'])


    @handler('data_received')
    def on_recv(self, sock, data):
        msg_type, msg, cmd_type, cmd = self._parser.decode(data)
        self.fire(msg_received(sock, msg_type, msg, cmd_type, cmd))


    @handler('send_msg')
    def on_send(self, sock, msg):
        data = self._parser.encode(msg)
        self.fire(send_data(sock, data))
