import wikitextparser as wtp
import json

from persistense import create_all_teams

file = open('teams.txt', mode='r')
text = file.read()
parsed = wtp.parse(text)

sections = []
sec_dict = []
for index, temp in enumerate(parsed.templates):
    if 'team=' in temp.string:
        # print(f'{index} -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        # print(temp)
        sections.append(temp)
        sec_dict.append({arg.name: arg.value.strip() for arg in temp.arguments})
# print(sections)
# print(json.dumps(sec_dict, indent=2))
create_all_teams(sec_dict)
