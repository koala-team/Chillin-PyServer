# -*- coding: utf-8 -*-

# python imports
import os
import struct

# circuits imports
from circuits import handler
from circuits.net.sockets import TCPServer
from circuits.net.events import write

# project imports
from ..config import Config
from ..events.network import data_received, client_disconnected
from ..helpers.logger import log


class Network(TCPServer):

    def __init__(self):
        self._read_clients = True
        self._buffer = {}

        bind = (Config.config['net']['host'], Config.config['net']['port'])

        if not (Config.config['net'].get('keyfile') and Config.config['net'].get('certfile')):
            certs_dir = os.path.join(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                'default_certs'
            )
            kwargs = dict(
                keyfile = os.path.join(certs_dir, 'key.pem'),
                certfile = os.path.join(certs_dir, 'cert.pem')
            )
        else:
            kwargs = dict(
                keyfile = Config.config['net']['keyfile'],
                certfile = Config.config['net']['certfile']
            )

        super(Network, self).__init__(bind, secure=True, **kwargs)
        log("Starting game server on host '%s' port %s ..." % bind)


    def _read(self, sock):
        if self._read_clients:
            super(Network, self)._read(sock)
        else:
            self._close(sock)


    @handler('stop_accepting')
    def on_stop_accepting(self):
        self._sock.close()


    @handler('stop_receiving')
    def on_stop_receiving(self):
        self._read_clients = False


    @handler('read')
    def on_read(self, sock, data):
        self._buffer[sock] += data
        while True:
            b = self._buffer[sock]
            if len(b) < 4:
                break

            size = struct.unpack('I', b[:4])[0]
            b = b[4:]
            if len(b) < size:
                break

            self.fire(data_received(sock, b[:size]))
            self._buffer[sock] = b[size:]


    @handler('send_data')
    def on_send(self, sock, data):
        size = struct.pack('I', len(data))
        self.fire(write(sock, size + data))


    @handler('connect')
    def on_connect(self, sock, host, port):
        self._buffer[sock] = b''


    @handler('disconnect')
    def on_disconnect(self, sock):
        self.fire(client_disconnected(sock))
        if sock in self._buffer:
            del self._buffer[sock]


    def busy(self):
        return True if self._poller._write else False
