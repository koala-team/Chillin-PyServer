# -*- coding: utf-8 -*-

# circuits imports
from circuits import Event


# to upper
class msg_received(Event):

    def __init__(self, sock, msg_type, msg, cmd_type, cmd):
        super(msg_received, self).__init__(
            sock = sock,
            msg_type = msg_type,
            msg = msg,
            cmd_type = cmd_type,
            cmd = cmd
        )


# from upper
class send_msg(Event):

    def __init__(self, sock, msg):
        super(send_msg, self).__init__(sock=sock, msg=msg)
