from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///wildtour.db3', echo=True)

Base = declarative_base()


class Team(Base):
    __tablename__ = 'team'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    tag = Column(String)


class Player(Base):
    __tablename__ = 'player'

    def __int__(self, nickname, team_id, flag, role):
        self.nickname = nickname
        self.team_id = team_id
        self.flag = flag
        self.role = role

    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String)
    team_id = Column(Integer, ForeignKey('team.id'))
    flag = Column(String)
    role = Column(String)


class Matchup(Base):
    __tablename__ = 'matchup'

    def __int__(self, datetime, phase, mvp, team1, team2):
        self.datetime = datetime
        self.phase = phase
        self.mvp_id = mvp
        self.team1 = team1
        self.team2 = team2

    id = Column(Integer, primary_key=True, autoincrement=True)
    phase = Column(String)
    datetime = Column(String)
    mvp_id = Column(Integer, ForeignKey('player.id'))
    team1 = Column(Integer, ForeignKey('team.id'))
    team2 = Column(Integer, ForeignKey('team.id'))


class MatchupMap(Base):
    __tablename__ = 'matchup_map'

    def __int__(self, matchup_id, map_number, blue_side, red_side, length, winner, winner_side,
                blue_baron_pick, blue_jungle_pick, blue_mid_pick, blue_dragon_pick, blue_sup_pick,
                red_baron_pick, red_jungle_pick, red_mid_pick, red_dragon_pick, red_sup_pick,
                blue_ban_1, blue_ban_2, blue_ban_3, blue_ban_4, blue_ban_5,
                red_ban_1, red_ban_2, red_ban_3, red_ban_4, red_ban_5,
                blue_baron_player, blue_jungle_player, blue_mid_player, blue_dragon_player, blue_sup_player,
                red_baron_player, red_jungle_player, red_mid_player, red_dragon_player, red_sup_player):
        self.match_id = matchup_id
        self.map_number = map_number
        self.blue_side = blue_side
        self.red_side = red_side
        self.length = length
        self.winner = winner
        self.winner_side = winner_side
        self.blue_baron_pick = blue_baron_pick
        self.blue_jungle_pick = blue_jungle_pick
        self.blue_mid_pick = blue_mid_pick
        self.blue_dragon_pick = blue_dragon_pick
        self.blue_sup_pick = blue_sup_pick
        self.red_baron_pick = red_baron_pick
        self.red_jungle_pick = red_jungle_pick
        self.red_mid_pick = red_mid_pick
        self.red_dragon_pick = red_dragon_pick
        self.red_sup_pick = red_sup_pick
        self.blue_ban_1 = blue_ban_1
        self.blue_ban_2 = blue_ban_2
        self.blue_ban_3 = blue_ban_3
        self.blue_ban_4 = blue_ban_4
        self.blue_ban_5 = blue_ban_5
        self.red_ban_1 = red_ban_1
        self.red_ban_2 = red_ban_2
        self.red_ban_3 = red_ban_3
        self.red_ban_4 = red_ban_4
        self.red_ban_5 = red_ban_5
        self.blue_baron_player = blue_baron_player
        self.blue_jungle_player = blue_jungle_player
        self.blue_mid_player = blue_mid_player
        self.blue_dragon_player = blue_dragon_player
        self.blue_sup_player = blue_sup_player
        self.red_baron_player = red_baron_player
        self.red_jungle_player = red_jungle_player
        self.red_mid_player = red_mid_player
        self.red_dragon_player = red_dragon_player
        self.red_sup_player = red_sup_player

    id = Column(Integer, primary_key=True, autoincrement=True)
    matchup_id = Column(Integer, ForeignKey('matchup.id'))
    map_number = Column(Integer, ForeignKey('player.id'))
    blue_side = Column(Integer, ForeignKey('team.id'))
    red_side = Column(Integer, ForeignKey('team.id'))
    length = Column(String)
    winner = Column(Integer, ForeignKey('team.id'))
    winner_side = Column(String)
    blue_baron_pick = Column(String)
    blue_jungle_pick = Column(String)
    blue_mid_pick = Column(String)
    blue_dragon_pick = Column(String)
    blue_sup_pick = Column(String)
    red_baron_pick = Column(String)
    red_jungle_pick = Column(String)
    red_mid_pick = Column(String)
    red_dragon_pick = Column(String)
    red_sup_pick = Column(String)
    blue_ban_1 = Column(String)
    blue_ban_2 = Column(String)
    blue_ban_3 = Column(String)
    blue_ban_4 = Column(String)
    blue_ban_5 = Column(String)
    red_ban_1 = Column(String)
    red_ban_2 = Column(String)
    red_ban_3 = Column(String)
    red_ban_4 = Column(String)
    red_ban_5 = Column(String)
    blue_baron_player = Column(Integer, ForeignKey('player.id'))
    blue_jungle_player = Column(Integer, ForeignKey('player.id'))
    blue_mid_player = Column(Integer, ForeignKey('player.id'))
    blue_dragon_player = Column(Integer, ForeignKey('player.id'))
    blue_sup_player = Column(Integer, ForeignKey('player.id'))
    red_baron_player = Column(Integer, ForeignKey('player.id'))
    red_mid_player = Column(Integer, ForeignKey('player.id'))
    red_jungle_player = Column(Integer, ForeignKey('player.id'))
    red_dragon_player = Column(Integer, ForeignKey('player.id'))
    red_sup_player = Column(Integer, ForeignKey('player.id'))


Base.metadata.create_all(engine)
