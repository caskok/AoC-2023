from collections import Counter

lines = open('input/input7.txt', 'r').readlines()
D = [line.strip().split() for line in lines]

card_map = {
    'T': 10,
    'J': 1,
    'Q': 12,
    'K': 13,
    'A': 14
}


class Hand:
    def __init__(self, hand_str: str, bet: int) -> None:
        hand = []
        self.jokers = 0
        for char in hand_str:
            if char.isdigit():
                hand.append(int(char))
                continue
            elif char == 'J':
                self.jokers += 1
            hand.append(card_map[char])

        self.hand = tuple(hand)
        score = Counter([card for card
                         in self.hand if card != 1]).most_common()
        self.score = [count for (_, count) in score]
        if not len(self.score):
            self.score = (5,)
        else:
            self.score[0] += self.jokers
        self.score = tuple(self.score)
        self.bet = bet

    def __lt__(self, other):
        if not isinstance(other, Hand):
            raise ValueError(f"{other} is not a Hand.")
        if other.score == self.score:
            return other.hand > self.hand
        return other.score > self.score

    def __repr__(self) -> str:
        return f"hand: {self.hand}, score: {self.score}, bet: {self.bet}"


hands = []
for cards, bet in D:
    hand = Hand(cards, int(bet))
    hands.append(hand)

hands.sort()
p1 = 0
for rank, hand in enumerate(hands, start=1):
    p1 += rank * hand.bet

print(p1)
