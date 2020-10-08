lang_family_group = {}
file = open('jezyki.txt', 'r')

next(file)
languages = [{'lang': line[0], 'family': line[1]} for line in map(lambda l: l.split('\t'), file.read().splitlines())]

for lang in languages:
    family = lang['family']
    lang_family_group[family] = 1 if family not in lang_family_group.keys() else lang_family_group[family] + 1

lang_family_group_arr = [{'lang': key, 'count': value} for key, value in lang_family_group.items()]
lang_family_group_arr.sort(key=lambda l: l['count'], reverse=True)

output_file = open('result.txt', 'a')
output_file.write('Zad 5.1\n\n')

for lang in lang_family_group_arr:
    output_file.write("{} {}\n".format(lang['lang'], lang['count']))
