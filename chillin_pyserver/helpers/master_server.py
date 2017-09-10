# -*- coding: utf-8 -*-


def get_token_info(token):
    team_id, agent_id = token.split('-')
    team_nickname = team_id + '.nickname'
    return team_id, agent_id, team_nickname


def send_match_result(match_id, winner_sidename, details):
    pass


def authenticate_spectator(token):
    return True
