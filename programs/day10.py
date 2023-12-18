from itertools import chain

lines = open('input/input10.txt', 'r').readlines()
D = [line.strip() for line in lines]


directions = ['NE', 'NW', 'NS', 'SE', 'SW', 'SN', 'WE',
              'WN', 'WS', 'EW', 'EN', 'ES', 'N', 'E', 'S', 'W']


class Pipe:
    def __init__(self, direction: str) -> None:
        if direction not in directions or len(direction) != 2:
            print(f"{direction} not valid.")
            assert False
        self.direction = direction
        self.direction_map = {direction[0]: direction[1],
                              direction[1]: direction[0]}

    def travel(self, from_direction: str):
        return self.direction_map[from_direction]


type_of_pipes = {
    '-': Pipe('EW'),
    '|': Pipe('NS'),
    'J': Pipe('NW'),
    '7': Pipe('SW'),
    'L': Pipe('NE'),
    'F': Pipe('SE'),
}

other_side = {
    'N': 'S',
    'S': 'N',
    'E': 'W',
    'W': 'E',
}


def coordinate_in_direction(i, j, direction):
    if len(direction) != 1:
        print(f"{direction} not valid.")
        assert False
    if direction == 'N':
        return i, j-1
    if direction == 'E':
        return i+1, j
    if direction == 'S':
        return i, j+1
    if direction == 'W':
        return i-1, j

    assert False


route = [[-1 for _ in line] for line in D]
visual = [['.' for _ in line] for line in D]

start = max([(string.find('S'), j) for j, string in enumerate(D)])
start_x, start_y = start[0], start[1]

visual[start_y][start_x] = '|'
route[start_y][start_x] = 0

moves = ['N', 'E', 'S', 'W']
node_queue = []

for move in moves:
    new_x, new_y = coordinate_in_direction(start_x, start_y, move)
    try:
        move_in_pipe = type_of_pipes[D[new_y][new_x]]
        new_direction = move_in_pipe.travel(other_side[move])
        score = 1
        node_queue.append(((new_x, new_y), new_direction, score))
        route[new_y][new_x] = score
        visual[new_y][new_x] = D[new_y][new_x]
    except KeyError:
        pass

while node_queue:
    (i, j), move, score = node_queue.pop(0)
    new_x, new_y = coordinate_in_direction(i, j, move)
    move_in_pipe = type_of_pipes[D[new_y][new_x]]
    new_direction = move_in_pipe.travel(other_side[move])
    if route[new_y][new_x] < 0:
        node_queue.append(((new_x, new_y), new_direction, score + 1))
        route[new_y][new_x] = score + 1
        visual[new_y][new_x] = D[new_y][new_x]

enclosed = 0
for line in visual:
    inside = False
    wall = ''
    for char in line:
        if char == '.' and inside:
            enclosed += 1
        elif char == '|':
            inside = not inside
        elif char in ['L', 'F']:
            wall = char
        elif wall and char == '7':
            if wall == 'L':
                inside = not inside
            wall = ''
        elif wall and char == 'J':
            if wall == 'F':
                inside = not inside
            wall = ''
print(max(list(chain.from_iterable(route))))
print(enclosed)
