# -*- coding: utf-8 -*-

# circuits imports
from circuits import Event


### to upper

class cmd_received(Event):

    def __init__(self, side_name, agent_name, msg, command_type, command):
        super(cmd_received, self).__init__(
            side_name = side_name,
            agent_name = agent_name,
            msg = msg,
            command_type = command_type,
            command = command
        )

class all_agents_joined(Event):

    def __init__(self):
        super(all_agents_joined, self).__init__()


### from upper

class broadcast_msg(Event):

    def __init__(self, msg, side_name=None, agent_name=None):
        super(broadcast_msg, self).__init__(
            msg = msg,
            side_name = side_name,
            agent_name = agent_name
        )
