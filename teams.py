import wikitextparser as wtp
import json

from persistense import create_all_teams

group = open('liquifiles/icons_group_teams.txt', mode='r').read()
play_in = open('liquifiles/icons_plain_teams.txt', mode='r').read()
parsed_group = wtp.parse(group)
parsed_play_in = wtp.parse(play_in)

sections = []
sec_dict = []
for index, temp in enumerate(parsed_group.templates):
    if '{{TeamCard\n' in temp.string:
        # print(f'{index} -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        # print(temp)
        # sections.append(temp)
        team = {arg.name: arg.value.strip() for arg in temp.arguments}
        team['phase'] = 'group'
        sec_dict.append(team)

for index, temp in enumerate(parsed_play_in.templates):
    if '{{TeamCard\n' in temp.string:
        # print(f'{index} -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        # print(temp)
        # sections.append(temp)
        team = {arg.name: arg.value.strip() for arg in temp.arguments}
        team['phase'] = 'play-in'
        sec_dict.append(team)
# print(sections)
print(json.dumps(sec_dict, indent=2))

create_all_teams(sec_dict)
