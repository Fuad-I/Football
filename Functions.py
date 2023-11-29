import os

replacement_table = {
    '\n': '',
    'âˆ’': '-',
    '?': '-',
    'é': 'e',
    'ñ': 'n',
    'á': 'a'
}


def get_season(filename):
    table = list()
    with open(filename, 'r') as f:
        for line in f:
            for k, v in replacement_table.items():
                line = line.replace(k, v)
            table.append(line.split(','))
    table.remove(table[0])
    return table


def update_seasons(path, teams):
    os.chdir(path)

    for file in os.listdir():
        for team in get_season(file):
            if team[0] in teams:
                teams[team[0]].update(file[:-4], [int(i) for i in team[1:]])
