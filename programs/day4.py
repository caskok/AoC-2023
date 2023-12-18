lines = open('input/input4.txt', 'r').readlines()
D = [line.strip().split(':')[1] for line in lines]

winning_numbers = [set(line.split('|')[0].split()) for line in D]
cards = [line.split('|')[1].split() for line in D]
matches = [0 for _ in D]
copies = [1 for _ in D]

total_profit = 0
for card_num, card in enumerate(cards):
    profit = 0
    for num in card:
        if num in winning_numbers[card_num]:
            matches[card_num] += 1
            if profit:
                profit *= 2
            else:
                profit = 1
    total_profit += profit

print(total_profit)

for card_num, match in enumerate(matches):
    for i in range(match):
        try:
            copies[card_num + i + 1] += copies[card_num]
        except IndexError:
            pass

print(sum(copies))
