users = {}

with open('uzytkownicy.txt', 'r') as file:
    next(file)
    for line in file.read().splitlines():
        split_line = line.split('\t')

        country, lang, population, formal = split_line

        if country not in users.keys():
            users[country] = {
                'country': country,
                'population': population,
                'languages': [{
                    'language': lang,
                    'formal': formal
                }]
            }
        else:
            users[country]['languages'].append({
                'language': lang,
                'formal': formal
            })

print(users)
