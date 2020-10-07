languages = set()
used_languages = set()

with open('jezyki.txt', 'r') as file:
    next(file)
    for line in file.read().splitlines():
        split_line = line.split('\t')
        languages.add(split_line[0])

with open('uzytkownicy.txt', 'r') as file:
    next(file)
    for line in file.read().splitlines():
        split_line = line.split('\t')

        if split_line[3] == 'tak':
            used_languages.add(split_line[1])


with open('result.txt', 'a') as result_file:
    result_file.write('\nZad 5.2\n')

    result_file.write("{}".format(len(languages - used_languages)))
