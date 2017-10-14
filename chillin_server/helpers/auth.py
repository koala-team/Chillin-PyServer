# -*- coding: utf-8 -*-

# python import
from pydblite import Base


class AgentAuthenticator:

    def __init__(self, sides, allowed_teams):
        self._sides = sides
        self._allowed_teams = allowed_teams
        self._create_agent_table()


    def _create_agent_table(self):
        agent_table = Base('agents', save_to_file=False)
        agent_table.create('sock', 'team_id', 'agent_id', 'side_name', 'agent_name')
        self._db = agent_table
        self._count_joined_teams = 0
        self._count_not_joined_agents = sum([len(agent_names) for agent_names in self._sides.values()])


    def is_joined(self, sock):
        return not (self._db(sock=sock) == [])


    def get_info(self, **kwargs):
        return self._db(**kwargs)


    def all_joined(self):
        return self._count_not_joined_agents == 0


    def join(self, sock, client_team_id, client_agent_id, client_agent_name):
        db = self._db
        ins_flag = False

        if not self._allowed_teams or client_team_id in self._allowed_teams:
            r = db(team_id=client_team_id)
            if r:
                side_name = r[0]['side_name']
                if client_agent_name in self._sides[side_name] and \
                        not db(side_name=side_name, agent_name=client_agent_name):
                    ins_flag = True
            else:
                side_name = sorted(list(self._sides.keys()))[self._count_joined_teams]
                side_name = self._allowed_teams.get(client_team_id, side_name)
                if client_agent_name in self._sides[side_name]:
                    ins_flag = True
                    self._count_joined_teams += 1

        if ins_flag:
            db.insert(
                sock = sock,
                team_id = client_team_id,
                agent_id = client_agent_id,
                side_name = side_name,
                agent_name = client_agent_name
            )

            self._count_not_joined_agents -= 1
            return side_name

        return ''
