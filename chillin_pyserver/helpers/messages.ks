[Message]
_def = class
type = string
payload = string


##########################################################
##########################################################

[JoinOfflineGame]
_def = class
team_nickname = string
agent_name = string


[JoinOnlineGame]
_def = class
token = string
agent_name = string


[ClientJoined]
_def = class
joined = boolean
side_name = string
sides = map <string, list<string> >


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


[BaseSnapshot]
_def = class
world_payload = string


[RealtimeSnapshot]
_def = class(BaseSnapshot)
current_cycle = uint
cycle_duration = float


[TurnbasedSnapshot]
_def = class(RealtimeSnapshot)
turn_allowed_sides = list <string>


##########################################################

[BaseCommand]
_def = class
type = string
payload = string


[RealtimeCommand]
_def = class(BaseCommand)
cycle = uint


[TurnbasedCommand]
_def = class(RealtimeCommand)
