languages = []
lang_family_group = {}
lang_family_group_arr = []

with open('jezyki.txt', 'r') as file:
    next(file)
    for line in file.read().splitlines():
        split_line = line.split('\t')

        languages.append({
            'lang': split_line[0],
            'family': split_line[1]
        })

for lang in languages:
    family = lang['family']

    if family not in lang_family_group.keys():
        lang_family_group[family] = 1
    else:
        lang_family_group[family] = lang_family_group[family] + 1

for lang_group_key in lang_family_group.keys():
    lang_family_group_arr.append({'lang': lang_group_key, 'count': lang_family_group[lang_group_key]})

lang_family_group_arr.sort(key=lambda l: l['count'], reverse=True)

with open('result.txt', 'a') as output_file:
    output_file.write('Zad 5.1\n\n')

    for lang in lang_family_group_arr:
        output_file.write("{} {}\n".format(lang['lang'], lang['count']))
