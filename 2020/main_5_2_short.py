with open('jezyki.txt', 'r') as file:
    next(file)
    languages = set([line.split('\t')[0] for line in file.read().splitlines()])

with open('uzytkownicy.txt', 'r') as file:
    next(file)
    used_languages = set([line[1] for line in map(lambda l: l.split('\t'), file.read().splitlines()) if line[3] == 'tak'])

with open('result.txt', 'a') as result_file:
    result_file.write("\nZad 5.2\n{}".format(len(languages - used_languages)))
