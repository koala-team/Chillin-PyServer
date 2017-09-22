# -*- coding: utf-8 -*-

# circuits imports
from circuits import Event


### to upper

class data_received(Event):

    def __init__(self, sock, data):
        super(data_received, self).__init__(sock=sock, data=data)


class client_disconnected(Event):

    def __init__(self, sock):
        super(client_disconnected, self).__init__(sock=sock)


### from upper

class send_data(Event):

    def __init__(self, sock, data):
        super(send_data, self).__init__(sock=sock, data=data)


class stop_accepting(Event):

    def __init__(self):
        super(stop_accepting, self).__init__()


class stop_receiving(Event):

    def __init__(self):
        super(stop_receiving, self).__init__()
