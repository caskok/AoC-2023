lines = open('input/input14.txt', 'r').readlines()
# lines = open('examples/ex14.txt', 'r').readlines()
D = [line.strip() for line in lines]

gap = '.'
boulder = '#'
stone = 'O'
stones = [boulder, stone]

new_config = [list(line) for line in D]


def rotate_matrix(matrix):
    temp_matrix = []
    column = len(matrix)-1
    for column in range(len(matrix)):
        temp = []
        for row in range(len(matrix) - 1, -1, -1):
            temp.append(matrix[row][column])
        temp_matrix.append(temp)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = temp_matrix[i][j]
    return matrix


DP = {}
old_config = tuple(new_config)

# Cycle lenght of 18 with an offset of 10 for 10000000000
cycles = 1810
cycle_config = []
for cycle in range(cycles):
    old_config = tuple(tuple(x) for x in new_config)
    if old_config in DP:
        new_config = DP[old_config]
    for dir in ['N', 'E', 'S', 'W']:
        last_stones = [-1 for _ in range(len(new_config[0]))]
        for row, line in enumerate(new_config):
            for boulder_col, item in enumerate(line):
                if item == '#':
                    last_stones[boulder_col] = row
                elif item == 'O':
                    last_stone = last_stones[boulder_col]
                    # is there already a stone above?
                    if last_stone == row - 1:
                        last_stones[boulder_col] += 1
                    # if not, move the stone up.
                    else:
                        assert new_config[last_stone + 1][boulder_col] == '.'
                        new_config[last_stone + 1][boulder_col] = 'O'
                        new_config[row][boulder_col] = '.'
                        last_stones[boulder_col] = last_stone + 1
        new_config = rotate_matrix(new_config)
    DP[old_config] = new_config

for item in new_config:
    print("".join(item))

p1 = 0
for row, line in enumerate(new_config):
    stones = line.count('O')
    p1 += (len(new_config) - row) * stones

print(p1)
