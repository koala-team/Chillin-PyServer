# -*- coding: utf-8 -*-

# python imports
from threading import Thread, Lock, Event
import sys

if sys.version_info > (3,):
    from queue import Queue
else:
    from Queue import Queue

# project imports
from ..config import Config
from ..helpers.logger import log
from .network import Network
from .parser import Parser
from .messages import Auth


class Protocol:

    def __init__(self, authenticate_func, game_info):
        self._auth_func = authenticate_func
        self._game_info = game_info
        self._all_messages_data = []
        self._network = Network()
        self._parser = Parser()
        self._clients = set()
        self._lock = Lock()
        self._running = Event()
        self.send_queue = Queue()


    def _add_client(self, sock):
        self._send_msg(sock, self._game_info)
        i = 0
        while i < len(self._all_messages_data):
            if not self._send_data(sock, self._all_messages_data[i]):
                self._network.close(sock)
                return
            i += 1

        # TODO: some messages may not get delivered here ...

        self._lock.acquire()
        self._clients.add(sock)
        self._lock.release()


    def _remove_clients(self, socks):
        for sock in socks:
            self._network.close(sock)
        self._lock.acquire()
        self._clients.difference_update(socks)
        self._lock.release()

        if len(socks) == 1:
            log("A spectator has left the game")
        elif len(socks) > 1:
            log("%s spectators have left the game" % len(socks))


    def _can_join(self, sock):
        if len(self._clients) >= Config.config['gui'].get('max_spectators', 5):
            return False
        return True


    def _accept(self):

        def init(sock):
            authenticated = False
            if Config.config['general']['offline_mode']:
                authenticated = True
            else:
                token = self._network.recv_data(sock)
                if token and self._auth_func(token):
                    authenticated = True
                    self._send_msg(sock, Auth(authenticated=True))
                else:
                    self._send_msg(sock, Auth(authenticated=False))
                    self._network.close(sock)

            if authenticated:
                self._add_client(sock)
                log("A spectator has joined the game")


        while self._running.is_set():
            sock = self._network.accept()
            if not self._can_join(sock):
                self._network.close(sock)
                continue

            if sock and self._running.is_set():
                t = Thread(target=init, args=(sock,))
                t.setDaemon(True)
                t.start()


    def _send_data(self, sock, data):
        return self._network.send_data(sock, data)


    def _send_msg(self, sock, msg):
        data = self._parser.encode(msg)
        return self._send_data(sock, data)


    def _broadcast_msg(self, msg):
        data = self._parser.encode(msg)
        self._all_messages_data.append(data)
        disconnected_clients = []
        for sock in self._clients:
            if not self._send_data(sock, data):
                disconnected_clients.append(sock)

        self._remove_clients(disconnected_clients)


    def _send_thread(self):
        while self._running.is_set():
            msg = self.send_queue.get()
            if msg:
                self._broadcast_msg(msg)


    def start(self):
        self._network.start()
        self._running.set()
        t = Thread(target=self._accept)
        t.setDaemon(True)
        t.start()
        t = Thread(target=self._send_thread)
        t.setDaemon(True)
        t.start()


    def stop(self):
        for sock in self._clients:
            self._network.close(sock)
        self._running.clear()
        self.send_queue.put(None)
        self._network.stop()
