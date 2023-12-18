lines = open('input/input3.txt', 'r').readlines()
D = [line.strip() for line in lines]


nums = {}
gears = {}


def search_left(x, y):
    res = ''
    try:
        while D[y][x - 1].isnumeric() and x > 0:
            res = D[y][x - 1] + res
            x -= 1
    except IndexError:
        pass
    return (x, y), res


def search_right(x, y):
    res = ''
    try:
        while D[y][x + 1].isnumeric():
            res += D[y][x + 1]
            x += 1
    except IndexError:
        pass

    return res


def add_numbers(x, y, sink):
    for i in [x-1, x, x+1]:
        for j in [y-1, y, y+1]:
            try:
                if D[j][i].isnumeric() and i > 0:
                    begin_index, left_side = search_left(i, j)
                    sink[begin_index] = int(left_side
                                            + D[j][i]
                                            + search_right(i, j))
            except IndexError:
                pass


for y, line in enumerate(D):
    for x, char in enumerate(line):
        if char.isnumeric() or char == '.':
            continue
        add_numbers(x, y, nums)
        if char == '*':
            gears[(x, y)] = {}
            add_numbers(x, y, gears[(x, y)])


print(sum(nums.values()))

total = 0
for gear in gears.values():
    if len(gear) == 2:
        g1, g2 = gear.values()
        total += g1 * g2
print(total)
