[Message]
_def = class
type = string
payload = string


##########################################################
##########################################################

[Auth]
_def = class
authenticated = boolean


[GameInfo]
_def = class
game_name = string
sides = map <string, list<string> >


##########################################################

[AgentJoined]
_def = class
side_name = string
agent_name = string
team_nickname = string


[AgentLeft]
_def = class
side_name = string
agent_name = string


##########################################################

[StartGame]
_def = class
start_time = uint


[EndGame]
_def = class
winner_sidename = string
details = map <string, map<string, string> >


##########################################################

[CanvasAction]
_def = class
action_types = list <string>
action_payloads = list <string>
