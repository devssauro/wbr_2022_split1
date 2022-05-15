from datetime import datetime
import wikitextparser as wtp
import json

from main import map_maker
from persistense import players_dict, teams_dict, create_all_matches

file = open('playoffs.txt', mode='r')
text = file.read()
parsed = wtp.parse(text)
p_dict = players_dict()
t_dict = teams_dict()

sections = []
sec_dict = []


for index, temp in enumerate(parsed.templates):
    if temp.string.startswith('{{Match\n'):
        # print(f'{index} -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        # print(temp)
        team1 = t_dict[[argument.value[15:-7] for argument in temp.arguments if argument.name == 'opponent1'][0]]
        team2 = t_dict[[argument.value[15:-7] for argument in temp.arguments if argument.name == 'opponent2'][0]]
        sections.append(temp)
        sec_dict.append({
            'phase': 'playoff',
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
