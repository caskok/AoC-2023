import numpy as np

lines = open('input/input8.txt', 'r').readlines()
D = [line.strip().split() for line in lines]

route = D[0][0]

nodes = {}

for line in D[2:]:
    nodes[line[0]] = (line[2][1:4], line[3][0:3])

steps = 0
current_location = 'AAA'

direction_map = {'L': 0, 'R': 1}

current_locations = [loc for loc in nodes.keys() if loc[-1] == 'A']
loops = [[] for _ in current_locations]


def are_we_finished(loops):
    for loop in loops:
        if len(loop) < 3:
            return False
    return True


while not are_we_finished(loops):
    step_in_route = route[steps % len(route)]
    direction = direction_map[step_in_route]
    next_locations = [nodes[loc][direction] for loc in current_locations]
    steps += 1
    current_locations = next_locations
    for i, loc in enumerate(current_locations):
        if loc[-1] == 'Z':
            loops[i].append(steps)

# take the path loop length (there is no offset).
paths = [loop[0] for loop in loops]
# gcd of all the paths.
gcd = np.gcd.reduce([loop[0] for loop in loops])

print(np.prod([path//gcd for path in paths]) * gcd)
