# Credit to Miklos for originally pointing out that the leaderboard is extractable as JSON
# Copied over from my 2021 repo
# not perfect - but good enough for now, prints to console a view of day scores & completion times for star 2 vs 1 show averages and flag unlikely efforts

from datetime import datetime
from termcolor import colored  # https://pypi.org/project/termcolor/
import json
with open('./Leaderboard/Day7.json') as f: 
    board = json.loads(f.read().strip())

data = list()
for m in board['members']:
    member = [board['members'][m]['name'], board['members'][m]['local_score'], board['members'][m]['stars'],dict()]
    for d in board['members'][m]['completion_day_level']:
        stars = len(board['members'][m]['completion_day_level'][d])
        t = int(board['members'][m]['completion_day_level'][d]['2']['get_star_ts']) - int(board['members'][m]['completion_day_level'][d]['1']['get_star_ts']) if stars == 2 else 0
        member[3][int(d)-1] = [stars, t] #datetime.utcfromtimestamp(t).strftime('%H:%M:%S')]
    data.append(member)

def sortKey(m): return m[1]
data.sort(key=sortKey, reverse=True) #sort by local rank
def star(num): return colored(''.join(['*' for a in range(num)]), 'yellow' if num == 2 else 'white')  

#print('{0:<3}   {1:<31} {2}'.format('#', 'Name (Stars)', ''.join(['{:<8} '.format(str(a)) for a in range(1, 25)])))
print('{0:},{1:},{2}'.format('#', 'Name,Stars', ''.join(['{:},'.format(str(a)) for a in range(1, 25)])))
for rank in range(len(data)): 
    #print('{:<3} - {:<25} ({:<2}) '.format(rank+1, str(data[rank][0]), data[rank][2]), 
    #    ''.join(['{0:<2} {1:<12} '.format(star(data[rank][3][a][0]), 
    #    colored(data[rank][3][a][1], 'red' if 0 < data[rank][3][a][1] < 90 else 'white')) for a in sorted(data[rank][3])]))

    print('{:},{:},{:},'.format(rank+1, str(data[rank][0]), data[rank][2]), 
        ''.join(['{0},{1},'.format(star(data[rank][3][a][0]), 
        colored(data[rank][3][a][1], 'red' if 0 < data[rank][3][a][1] < 90 else 'white')) for a in sorted(data[rank][3])]))