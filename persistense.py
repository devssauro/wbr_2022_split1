from typing import List

from sqlalchemy.orm import sessionmaker
from db import Team, engine, Player, Matchup, MatchupMap

Session = sessionmaker(bind=engine)
# session = Session()


def create_all_teams(data: List[dict]):
    session = Session()
    for team in data:
        team_obj = Team()
        team_obj.name = team['team']
        session.add(team_obj)
        session.commit()
        baron = Player(nickname=team['p1'], flag=team['p1flag'], team_id=team_obj.id, role='baron')
        jungle = Player(nickname=team['p2'], flag=team['p2flag'], team_id=team_obj.id, role='jungle')
        mid = Player(nickname=team['p3'], flag=team['p3flag'], team_id=team_obj.id, role='mid')
        dragon = Player(nickname=team['p4'], flag=team['p4flag'], team_id=team_obj.id, role='dragon')
        sup = Player(nickname=team['p5'], flag=team['p5flag'], team_id=team_obj.id, role='sup')
        session.add(baron)
        session.add(jungle)
        session.add(mid)
        session.add(dragon)
        session.add(sup)
    session.commit()
    session.close()


def create_all_matches(data: List[dict]):
    session = Session()
    for match in data:
        matchup = Matchup()
        matchup.mvp_id = match['mvp']
        matchup.datetime = match['datetime']
        matchup.team1 = match['team1']
        matchup.team2 = match['team2']
        matchup.phase = match['phase']
        session.add(matchup)
        session.commit()
        for map in match['maps']:
            mmap = MatchupMap(matchup_id=matchup.id, **map)
            session.add(mmap)
        session.commit()
    session.close()


def players_dict() -> dict:
    session = Session()
    return {player.nickname: player.id for player in session.query(Player).all()}


def teams_dict() -> dict:
    session = Session()
    return {
        **{team.name.lower(): team.id for team in session.query(Team).all()},
        **{team.tag.lower(): team.id for team in session.query(Team).all()}
    }


def teams_ids(team_id, side) -> dict:
    session = Session()
    players = session.query(Player).distinct(Player.role).filter(
        Player.team_id == team_id
    ).order_by(Player.id.desc())
    session.close()
    return {f'{side}_{player.role}_player': player.id for player in players}