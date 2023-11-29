STAT_NAMES = ['MP', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Pts']


class Team:

    def __init__(self, name):
        self.name = name
        self.seasons = dict()

    def update(self, season, stats):
        self.seasons[season] = {k: v for k, v in zip(STAT_NAMES, stats)}

    def get_stat(self, stat):
        return [v[stat] for k, v in self.seasons.items()]


class Player:

    def __init__(self, name, team=None, stats=None):
        self.name = name
        self.team = team
        self.stats = stats
