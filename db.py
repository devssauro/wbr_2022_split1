from sqlalchemy import Column, Integer, Text, ForeignKey, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///icons.db3', echo=True)

Base = declarative_base()


class Team(Base):
    __tablename__ = 'team'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text)
    tag = Column(Text)
    flag = Column(Text)
    phase = Column(Text)


class Player(Base):
    __tablename__ = 'player'

    def __int__(self, nickname, team_id, flag, role):
        self.nickname = nickname
        self.team_id = team_id
        self.flag = flag
        self.role = role

    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(Text)
    team_id = Column(Integer, ForeignKey('team.id'))
    flag = Column(Text)
    role = Column(Text)


class Matchup(Base):
    __tablename__ = 'matchup'

    def __int__(self, datetime, phase, mvp, team1, team2):
        self.datetime = datetime
        self.phase = phase
        self.mvp_id = mvp
        self.team1 = team1
        self.team2 = team2

    id = Column(Integer, primary_key=True, autoincrement=True)
    phase = Column(Text)
    datetime = Column(Text)
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
                blue_pick_1, blue_pick_2, blue_pick_3, blue_pick_4, blue_pick_5,
                red_pick_1, red_pick_2, red_pick_3, red_pick_4, red_pick_5,
                blue_baron_kills, blue_jungle_kills, blue_mid_kills, blue_dragon_kills, blue_sup_kills,
                red_baron_kills, red_jungle_kills, red_mid_kills, red_dragon_kills, red_sup_kills,
                blue_baron_deaths, blue_jungle_deaths, blue_mid_deaths, blue_dragon_deaths, blue_sup_deaths,
                red_baron_deaths, red_jungle_deaths, red_mid_deaths, red_dragon_deaths, red_sup_deaths,
                blue_baron_assists, blue_jungle_assists, blue_mid_assists, blue_dragon_assists, blue_sup_assists,
                red_baron_assists, red_jungle_assists, red_mid_assists, red_dragon_assists, red_sup_assists,
                blue_baron_dmg_taken, blue_jungle_dmg_taken, blue_mid_dmg_taken, blue_dragon_dmg_taken, blue_sup_dmg_taken,
                red_baron_dmg_taken, red_jungle_dmg_taken, red_mid_dmg_taken, red_dragon_dmg_taken, red_sup_dmg_taken,
                blue_baron_dmg_dealt, blue_jungle_dmg_dealt, blue_mid_dmg_dealt, blue_dragon_dmg_dealt, blue_sup_dmg_dealt,
                red_baron_dmg_dealt, red_jungle_dmg_dealt, red_mid_dmg_dealt, red_dragon_dmg_dealt, red_sup_dmg_dealt,
                blue_baron_total_gold, blue_jungle_total_gold, blue_mid_total_gold, blue_dragon_total_gold, blue_sup_total_gold,
                red_baron_total_gold, red_jungle_total_gold, red_mid_total_gold, red_dragon_total_gold, red_sup_total_gold,
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
        self.blue_pick_1 = blue_pick_1
        self.blue_pick_2 = blue_pick_2
        self.blue_pick_3 = blue_pick_3
        self.blue_pick_4 = blue_pick_4
        self.blue_pick_5 = blue_pick_5
        self.red_pick_1 = red_pick_1
        self.red_pick_2 = red_pick_2
        self.red_pick_3 = red_pick_3
        self.red_pick_4 = red_pick_4
        self.red_pick_5 = red_pick_5
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
        self.blue_baron_kills = blue_baron_kills
        self.blue_jungle_kills = blue_jungle_kills
        self.blue_mid_kills = blue_mid_kills
        self.blue_dragon_kills = blue_dragon_kills
        self.blue_sup_kills = blue_sup_kills
        self.red_baron_kills = red_baron_kills
        self.red_jungle_kills = red_jungle_kills
        self.red_mid_kills = red_mid_kills
        self.red_dragon_kills = red_dragon_kills
        self.red_sup_kills = red_sup_kills
        self.blue_baron_deaths = blue_baron_deaths
        self.blue_jungle_deaths = blue_jungle_deaths
        self.blue_mid_deaths = blue_mid_deaths
        self.blue_dragon_deaths = blue_dragon_deaths
        self.blue_sup_deaths = blue_sup_deaths
        self.red_baron_deaths = red_baron_deaths
        self.red_jungle_deaths = red_jungle_deaths
        self.red_mid_deaths = red_mid_deaths
        self.red_dragon_deaths = red_dragon_deaths
        self.red_sup_deaths = red_sup_deaths
        self.blue_baron_assists = blue_baron_assists
        self.blue_jungle_assists = blue_jungle_assists
        self.blue_mid_assists = blue_mid_assists
        self.blue_dragon_assists = blue_dragon_assists
        self.blue_sup_assists = blue_sup_assists
        self.red_baron_assists = red_baron_assists
        self.red_jungle_assists = red_jungle_assists
        self.red_mid_assists = red_mid_assists
        self.red_dragon_assists = red_dragon_assists
        self.red_sup_assists = red_sup_assists
        self.blue_baron_dmg_taken = blue_baron_dmg_taken
        self.blue_jungle_dmg_taken = blue_jungle_dmg_taken
        self.blue_mid_dmg_taken = blue_mid_dmg_taken
        self.blue_dragon_dmg_taken = blue_dragon_dmg_taken
        self.blue_sup_dmg_taken = blue_sup_dmg_taken
        self.red_baron_dmg_taken = red_baron_dmg_taken
        self.red_jungle_dmg_taken = red_jungle_dmg_taken
        self.red_mid_dmg_taken = red_mid_dmg_taken
        self.red_dragon_dmg_taken = red_dragon_dmg_taken
        self.red_sup_dmg_taken = red_sup_dmg_taken
        self.blue_baron_dmg_dealt = blue_baron_dmg_dealt
        self.blue_jungle_dmg_dealt = blue_jungle_dmg_dealt
        self.blue_mid_dmg_dealt = blue_mid_dmg_dealt
        self.blue_dragon_dmg_dealt = blue_dragon_dmg_dealt
        self.blue_sup_dmg_dealt = blue_sup_dmg_dealt
        self.red_baron_dmg_dealt = red_baron_dmg_dealt
        self.red_jungle_dmg_dealt = red_jungle_dmg_dealt
        self.red_mid_dmg_dealt = red_mid_dmg_dealt
        self.red_dragon_dmg_dealt = red_dragon_dmg_dealt
        self.red_sup_dmg_dealt = red_sup_dmg_dealt
        self.blue_baron_total_gold = blue_baron_total_gold
        self.blue_jungle_total_gold = blue_jungle_total_gold
        self.blue_mid_total_gold = blue_mid_total_gold
        self.blue_dragon_total_gold = blue_dragon_total_gold
        self.blue_sup_total_gold = blue_sup_total_gold
        self.red_baron_total_gold = red_baron_total_gold
        self.red_jungle_total_gold = red_jungle_total_gold
        self.red_mid_total_gold = red_mid_total_gold
        self.red_dragon_total_gold = red_dragon_total_gold
        self.red_sup_total_gold = red_sup_total_gold

    id = Column(Integer, primary_key=True, autoincrement=True)
    matchup_id = Column(Integer, ForeignKey('matchup.id'))
    map_number = Column(Integer)
    blue_side = Column(Integer, ForeignKey('team.id'))
    red_side = Column(Integer, ForeignKey('team.id'))
    length = Column(Text)
    winner = Column(Integer, ForeignKey('team.id'))
    winner_side = Column(Text)
    blue_ban_1 = Column(Text)
    red_ban_1 = Column(Text)
    blue_ban_2 = Column(Text)
    red_ban_2 = Column(Text)
    blue_ban_3 = Column(Text)
    red_ban_3 = Column(Text)
    blue_pick_1 = Column(Text)
    red_pick_1 = Column(Text)
    red_pick_2 = Column(Text)
    blue_pick_2 = Column(Text)
    blue_pick_3 = Column(Text)
    red_pick_3 = Column(Text)
    blue_ban_4 = Column(Text)
    red_ban_4 = Column(Text)
    blue_ban_5 = Column(Text)
    red_ban_5 = Column(Text)
    red_pick_4 = Column(Text)
    blue_pick_4 = Column(Text)
    blue_pick_5 = Column(Text)
    red_pick_5 = Column(Text)
    blue_baron_pick = Column(Text)
    blue_jungle_pick = Column(Text)
    blue_mid_pick = Column(Text)
    blue_dragon_pick = Column(Text)
    blue_sup_pick = Column(Text)
    red_baron_pick = Column(Text)
    red_jungle_pick = Column(Text)
    red_mid_pick = Column(Text)
    red_dragon_pick = Column(Text)
    red_sup_pick = Column(Text)
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
    blue_baron_kills = Column(Integer, default=0)
    blue_jungle_kills = Column(Integer, default=0)
    blue_mid_kills = Column(Integer, default=0)
    blue_dragon_kills = Column(Integer, default=0)
    blue_sup_kills = Column(Integer, default=0)
    red_baron_kills = Column(Integer, default=0)
    red_jungle_kills = Column(Integer, default=0)
    red_mid_kills = Column(Integer, default=0)
    red_dragon_kills = Column(Integer, default=0)
    red_sup_kills = Column(Integer, default=0)
    blue_baron_deaths = Column(Integer, default=0)
    blue_jungle_deaths = Column(Integer, default=0)
    blue_mid_deaths = Column(Integer, default=0)
    blue_dragon_deaths = Column(Integer, default=0)
    blue_sup_deaths = Column(Integer, default=0)
    red_baron_deaths = Column(Integer, default=0)
    red_jungle_deaths = Column(Integer, default=0)
    red_mid_deaths = Column(Integer, default=0)
    red_dragon_deaths = Column(Integer, default=0)
    red_sup_deaths = Column(Integer, default=0)
    blue_baron_assists = Column(Integer, default=0)
    blue_jungle_assists = Column(Integer, default=0)
    blue_mid_assists = Column(Integer, default=0)
    blue_dragon_assists = Column(Integer, default=0)
    blue_sup_assists = Column(Integer, default=0)
    red_baron_assists = Column(Integer, default=0)
    red_jungle_assists = Column(Integer, default=0)
    red_mid_assists = Column(Integer, default=0)
    red_dragon_assists = Column(Integer, default=0)
    red_sup_assists = Column(Integer, default=0)
    blue_baron_dmg_taken = Column(Integer, default=0)
    blue_jungle_dmg_taken = Column(Integer, default=0)
    blue_mid_dmg_taken = Column(Integer, default=0)
    blue_dragon_dmg_taken = Column(Integer, default=0)
    blue_sup_dmg_taken = Column(Integer, default=0)
    red_baron_dmg_taken = Column(Integer, default=0)
    red_jungle_dmg_taken = Column(Integer, default=0)
    red_mid_dmg_taken = Column(Integer, default=0)
    red_dragon_dmg_taken = Column(Integer, default=0)
    red_sup_dmg_taken = Column(Integer, default=0)
    blue_baron_dmg_dealt = Column(Integer, default=0)
    blue_jungle_dmg_dealt = Column(Integer, default=0)
    blue_mid_dmg_dealt = Column(Integer, default=0)
    blue_dragon_dmg_dealt = Column(Integer, default=0)
    blue_sup_dmg_dealt = Column(Integer, default=0)
    red_baron_dmg_dealt = Column(Integer, default=0)
    red_jungle_dmg_dealt = Column(Integer, default=0)
    red_mid_dmg_dealt = Column(Integer, default=0)
    red_dragon_dmg_dealt = Column(Integer, default=0)
    red_sup_dmg_dealt = Column(Integer, default=0)
    blue_baron_total_gold = Column(Integer, default=0)
    blue_jungle_total_gold = Column(Integer, default=0)
    blue_mid_total_gold = Column(Integer, default=0)
    blue_dragon_total_gold = Column(Integer, default=0)
    blue_sup_total_gold = Column(Integer, default=0)
    red_baron_total_gold = Column(Integer, default=0)
    red_jungle_total_gold = Column(Integer, default=0)
    red_mid_total_gold = Column(Integer, default=0)
    red_dragon_total_gold = Column(Integer, default=0)
    red_sup_total_gold = Column(Integer, default=0)


Base.metadata.create_all(engine)
