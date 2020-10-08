lang_file = open('jezyki.txt', 'r')
users_file = open('uzytkownicy.txt', 'r')
result_file = open('result.txt', 'a')

next(lang_file)
next(users_file)

languages = set([line.split('\t')[0] for line in lang_file.read().splitlines()])
used_languages = set([line[1] for line in map(lambda l: l.split('\t'), users_file.read().splitlines()) if line[3] == 'tak'])

result_file.write("\nZad 5.2\n{}".format(len(languages - used_languages)))
