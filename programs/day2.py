lines = open('input/input2.txt', 'r').readlines()
D = [line.strip().split(':')[1] for line in lines]

games = []
for line in D:
    min_dice = {}
    for handfull in line.split(';'):
        for dice in handfull.split(','):
            amount, color = dice.split()
            min_dice[color] = max(min_dice.get(color, 0), int(amount))
    games.append(min_dice)

p1 = 0
for game, dice in enumerate(games, start=1):
    if dice['red'] > 12:
        continue
    if dice['green'] > 13:
        continue
    if dice['blue'] > 14:
        continue

    p1 += game

p2 = 0
for dice in games:
    p2 += (dice['red'] * dice['green'] * dice['blue'])


print(p1)
print(p2)
