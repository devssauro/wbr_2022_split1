from datetime import datetime
import wikitextparser as wtp
import json

from persistense import players_dict, teams_dict, teams_ids, create_all_matches

file = open('group_stage.txt', mode='r')
text = file.read()
parsed = wtp.parse(text)
p_dict = players_dict()
t_dict = teams_dict()

sections = []
sec_dict = []


def map_maker(map, map_number):
    if not [argument.value.strip() for argument in map.arguments if argument.name == 'length'][0]:
        return None
    blue_side = team1 if [argument.value.strip() for argument in map.arguments
                          if argument.name == 'team1side'][0] == 'blue' else team2
    red_side = team1 if [argument.value.strip() for argument in map.arguments
                         if argument.name == 'team1side'][0] == 'red' else team2
    winner = team1 if [argument.value.split('\n')[0].strip() for argument in map.arguments
                       if argument.name == 'winner'][0] == '1' else team2
    return {
        'map_number': map_number,
        'blue_side': blue_side,
        'red_side': red_side,
        'length': [argument.value.strip() for argument in map.arguments if argument.name == 'length'][0],
        'winner': winner,
        'winner_side': 'blue' if winner == blue_side else 'red',
        # picks
        'blue_baron_pick': [
            argument.value.strip() for argument in map.arguments if argument.name == 't1c1'][0],
        'blue_jungle_pick': [
            argument.value.strip() for argument in map.arguments if argument.name == 't1c2'][0],
        'blue_mid_pick': [
            argument.value.strip() for argument in map.arguments if argument.name == 't1c3'][0],
        'blue_dragon_pick': [
            argument.value.strip() for argument in map.arguments if argument.name == 't1c4'][0],
        'blue_sup_pick': [
            argument.value.strip() for argument in map.arguments if argument.name == 't1c5'][0],
        'red_baron_pick': [
            argument.value.strip() for argument in map.arguments if argument.name == 't2c1'][0],
        'red_jungle_pick': [
            argument.value.strip() for argument in map.arguments if argument.name == 't2c2'][0],
        'red_mid_pick': [
            argument.value.strip() for argument in map.arguments if argument.name == 't2c3'][0],
        'red_dragon_pick': [
            argument.value.strip() for argument in map.arguments if argument.name == 't2c4'][0],
        'red_sup_pick': [
            argument.value.strip() for argument in map.arguments
            if argument.name == 't2c5'][0].split('\n')[0],
        # bans
        'blue_ban_1': [
            argument.value.strip() for argument in map.arguments if argument.name == 't1b1'][0],
        'blue_ban_2': [
            argument.value.strip() for argument in map.arguments if argument.name == 't1b2'][0],
        'blue_ban_3': [
            argument.value.strip() for argument in map.arguments if argument.name == 't1b3'][0],
        'blue_ban_4': [
            argument.value.strip() for argument in map.arguments if argument.name == 't1b4'][0],
        'blue_ban_5': [
            argument.value.strip() for argument in map.arguments if argument.name == 't1b5'][0],
        'red_ban_1': [
            argument.value.strip() for argument in map.arguments if argument.name == 't2b1'][0],
        'red_ban_2': [
            argument.value.strip() for argument in map.arguments if argument.name == 't2b2'][0],
        'red_ban_3': [
            argument.value.strip() for argument in map.arguments if argument.name == 't2b3'][0],
        'red_ban_4': [
            argument.value.strip() for argument in map.arguments if argument.name == 't2b4'][0],
        'red_ban_5': [
            argument.value.strip() for argument in map.arguments
            if argument.name == 't2c5'][0].split('\n')[0],
        # players
        **teams_ids(blue_side, 'blue'),
        **teams_ids(red_side, 'red'),
    }


for index, temp in enumerate(parsed.templates):
    if temp.string.startswith('{{Match\n'):
        # print(f'{index} -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        # print(temp)
        team1 = t_dict[[argument.value[15:-7] for argument in temp.arguments if argument.name == 'opponent1'][0]]
        team2 = t_dict[[argument.value[15:-7] for argument in temp.arguments if argument.name == 'opponent2'][0]]
        sections.append(temp)
        sec_dict.append({
            'phase': 'group',
            'mvp': p_dict[[argument.value.strip() for argument in temp.arguments if argument.name == 'mvp'][0]],
            'datetime': datetime.strptime(
                [argument.value for argument in temp.arguments if argument.name == 'date'][0][0:-13],
                '%B %d, %Y - %H:%M').isoformat(),
            'team1': team1,
            'team2': team2,
            'maps': [m for m in [map_maker(arg.templates[0], int(arg.name[-1])) for arg in temp.arguments
                     if 'map' in arg.name] if m is not None]
        })


# print(sections)
print(json.dumps(sec_dict, indent=2))
create_all_matches(sec_dict)
