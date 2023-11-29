import matplotlib.pyplot as plt
import numpy as np
from Classes import Team
from Functions import update_seasons

TEAMS_LA_LIGA = {
    'Barcelona': Team('Barcelona'),
    'Atletico Madrid': Team('Atletico Madrid'),
    'Real Madrid': Team('Real Madrid'),
    'Sevilla': Team('Sevilla'),
    'Valencia': Team('Valencia')
}

TEAMS_EPL = {
    'Manchester City': Team('Manchester City'),
    'Liverpool': Team('Liverpool'),
    'Manchester United': Team('Manchester United'),
    'Tottenham Hotspur': Team('Tottenham Hotspur'),
    'Arsenal': Team('Arsenal'),
    'Leicester City': Team('Leicester City'),
    'Chelsea': Team('Chelsea')
}

update_seasons('\\Users\\crioi\\PycharmProjects\\Football\\La Liga', TEAMS_LA_LIGA)
update_seasons('\\Users\\crioi\\PycharmProjects\\Football\\EPL', TEAMS_EPL)

seasons = ['{}-{}'.format(i, i + 1) for i in range(5, 20)]

#plt.plot(seasons, TEAMS_LA_LIGA['Barcelona'].get_stat('Pts')[3:-1], linestyle='dashed', marker='o', markerfacecolor='red', markersize=6, label='Barca')
#plt.plot(seasons, TEAMS_EPL['Manchester City'].get_stat('Pts'), linestyle='dashed', marker='o', markerfacecolor='blue', markersize=6,  label='Man City')

barWidth = 0.25
br1 = np.arange(len(seasons))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]

plt.bar(br1, TEAMS_LA_LIGA['Barcelona'].get_stat('Pts'), color ='r', width = barWidth, edgecolor ='grey', label ='Barca')
#plt.bar(br2, TEAMS_EPL['Manchester City'].get_stat('Pts'), color ='b', width = barWidth, edgecolor ='grey', label ='Man City')
plt.bar(br2, TEAMS_LA_LIGA['Real Madrid'].get_stat('Pts'), color ='b', width = barWidth, edgecolor ='grey', label ='Real Madrid')

#plt.ylim(0,114)
#plt.xlim(1,8)

plt.xlabel('Season')
plt.ylabel('Points')
plt.title('La Liga')

plt.xticks([r + barWidth for r in range(len(seasons))],
           seasons)

plt.legend()
plt.show()
