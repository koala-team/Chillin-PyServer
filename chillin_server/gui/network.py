# -*- coding: utf-8 -*-

# python imports
import os
import struct
from socket import socket, SOL_SOCKET, SO_REUSEADDR, IPPROTO_TCP, TCP_NODELAY
from ssl import wrap_socket

# project imports
from ..config import Config
from ..helpers.logger import log
from .parser import Parser


class Network:

    def __init__(self):
        self._bind = (Config.config['gui']['host'], Config.config['gui']['port'])
        self._sock = self._create_socket()


    def _create_socket(self):
        if not (Config.config['net'].get('keyfile') and Config.config['net'].get('certfile')):
            certs_dir = os.path.join(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                'default_certs'
            )
            keyfile = os.path.join(certs_dir, 'key.pem')
            certfile = os.path.join(certs_dir, 'cert.pem')
        else:
            keyfile = Config.config['net']['keyfile']
            certfile = Config.config['net']['certfile']

        sock = socket()
        sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        sock.setsockopt(IPPROTO_TCP, TCP_NODELAY, 1)
        return wrap_socket(sock, keyfile=keyfile, certfile=certfile)


    def start(self):
        self._sock.bind(self._bind)
        self._sock.listen(5)
        log("Starting gui server on host '%s' port %s ..." % self._bind)


    def stop(self):
        try:
            wrap_socket(socket()).connect(self._bind)
            self.close()
        except:
            pass


    def accept(self):
        try:
            sock, _ = self._sock.accept()
            sock.settimeout(1)
            return sock
        except:
            return None


    def recv_data(self, sock):
        try:
            size = sock.recv(4)
            if not size:
                return b''
            size = struct.unpack('I', size)[0]
            data = b''
            while len(data) < size:
                tmp = sock.recv(min(1024, size - len(data)))
                if not tmp:
                    return b''
                data += tmp
            return Parser.get_string(data)
        except:
            return b''


    def send_data(self, sock, data):
        try:
            size = struct.pack('I', len(data))
            return sock.send(size + data)
        except:
            return None


    def close(self, sock=None):
        if sock:
            sock.close()
        else:
            self._sock.close()
