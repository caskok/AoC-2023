lines = open('input/input16.txt', 'r').readlines()
# lines = open('examples/ex16a.txt', 'r').readlines()
D = [line.strip() for line in lines]

beams = []
traveled = [[[] for _ in D[0]] for _ in D]


class Beam:
    def __init__(self, x, y, direction) -> None:
        self.x = x
        self.y = y
        self.direction = direction

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Beam):
            return False
        return (self.x == __value.x
                and self.y == __value.y
                and self.direction == __value.direction)

    def __repr__(self) -> str:
        return f"({self.x},{self.y}) {self.direction}"

    def mark_position(self) -> None:
        global traveled
        if self.direction in traveled[self.y][self.x]:
            raise ValueError

        traveled[self.y][self.x].append(self.direction)

    def step(self):
        """Make a single step."""
        x_step = 1 if self.direction == 'E' else (-1 if self.direction == 'W'
                                                  else 0)
        y_step = 1 if self.direction == 'S' else (-1 if self.direction == 'N'
                                                  else 0)
        self.mark_position()
        new_x = self.x + x_step
        new_y = self.y + y_step

        if new_x < 0 or new_x >= len(D[0]) or new_y < 0 or new_y >= len(D):
            raise IndexError
        self.x += x_step
        self.y += y_step

    def travel_to_obstacle(self) -> None:
        while D[self.y][self.x] == '.':
            self.step()

    def handle_obstacle(self) -> None:
        global beams
        obstacle_type = D[self.y][self.x]
        assert obstacle_type != '.'
        obstacle = Obstacle(obstacle_type)

        new_direction = obstacle.reflect(self.direction)
        if len(new_direction) == 2:
            new_beam = Beam(self.x, self.y, new_direction[1])
            beams.append(new_beam)

        self.direction = new_direction[0]


class Obstacle:
    def __init__(self, symbol) -> None:
        self.is_splitter = symbol in ['|', '-']
        if symbol == '/':
            self.reflection_dict = {
                'S': 'W',
                'E': 'N',
                'N': 'E',
                'W': 'S',
            }
        elif symbol == '\\':
            self.reflection_dict = {
                'S': 'E',
                'E': 'S',
                'N': 'W',
                'W': 'N',
            }
        elif symbol == '|':
            self.reflection_dict = {
                'N': 'N',
                'S': 'S',
                'E': 'SN',
                'W': 'SN',
            }
        elif symbol == '-':
            self.reflection_dict = {
                'E': 'E',
                'W': 'W',
                'N': 'WE',
                'S': 'WE',
            }

    def reflect(self, direction):
        assert len(direction) == 1
        return self.reflection_dict[direction]


def get_energy_count(start_x, start_y, start_direction):
    global traveled
    global beams
    beams = []
    traveled = [[[] for _ in D[0]] for _ in D]
    beams.append(Beam(start_x, start_y, start_direction))
    while beams:
        beam = beams.pop()
        try:
            beam.travel_to_obstacle()
            beam.handle_obstacle()
            beam.step()
            beams.append(beam)
        except (IndexError, ValueError):
            pass

    return (sum([sum([1 for dirs in rows if len(dirs)]) for rows in traveled]))


def get_max_energy_count():
    max_count = 0

    for x in range(len(D[0])):
        max_count = max(max_count, get_energy_count(x, 0, 'S'))
        max_count = max(max_count, get_energy_count(x, len(D)-1, 'N'))
    for y in range(len(D)):
        max_count = max(max_count, get_energy_count(0, y, 'E'))
        max_count = max(max_count, get_energy_count(len(D[0])-1, y, 'W'))

    return max_count


if __name__ == '__main__':
    print("part 1:", get_energy_count(0, 0, 'E'))
    print("part 2:", get_max_energy_count())


""" debug = {
    'N': '^',
    'S': 'v',
    'E': '>',
    'W': '<',
}
debug_list = [[[debug[direc] for direc in item] for item in row]
              for row in traveled]
print_type = ''
for j, row in enumerate(debug_list):
    string = ''
    for i, item in enumerate(row):
        if print_type:
            if len(item) == 0:
                string += '.'
            else:
                string += '#'
        else:
            if D[j][i] != '.':
                string += D[j][i]
            elif len(item) == 0:
                string += '.'
            elif len(item) == 1:
                string += item[0]
            else:
                string += str(len(item))
    print(string) """
