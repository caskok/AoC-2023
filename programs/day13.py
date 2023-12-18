from itertools import groupby

lines = open('input/input13.txt', 'r').readlines()
# lines = open('examples/ex13.txt', 'r').readlines()
D = [[line.strip() for line in list(g)] for k, g
     in groupby(lines, key=lambda x: x != '\n') if k]


def find_row_mirror(grid):
    reverse_grid = list(reversed(grid))
    for i in range(1, len(grid)):
        all_are_equal = True
        for a, b in zip(grid[i:], reverse_grid[-i:]):
            if a != b:
                all_are_equal = False
                break
        if all_are_equal:
            return i


def find_col_mirror(grid):
    for i in range(len(grid[0])):
        all_are_equal = True
        print(i)
        for line in grid:
            print(line)
            reversed_line = list(reversed(line))
            for a, b in zip(line[i:], reversed_line[-i:]):
                print(a, b)
                if a != b:
                    all_are_equal = False
                    break
            if not all_are_equal:
                break
        if all_are_equal:
            return i


def find_second_row_mirror(grid):
    reverse_grid = list(reversed(grid))
    for i in range(1, len(grid)):
        all_are_equal = True
        only_one = False
        for a, b in zip(grid[i:], reverse_grid[-i:]):
            for item_a, item_b in zip(a, b):
                if item_a != item_b:
                    if not only_one:
                        only_one = True
                    else:
                        all_are_equal = False
                        break
            if not all_are_equal:
                break
        if all_are_equal and only_one:
            return i


def find_second_col_mirror(grid):
    for i in range(len(grid[0])):
        all_are_equal = True
        only_one = False
        for line in grid:
            reversed_line = list(reversed(line))
            for a, b in zip(line[i:], reversed_line[-i:]):
                if a != b:
                    if not only_one:
                        only_one = True
                    else:
                        all_are_equal = False
                        break
            if not all_are_equal:
                break
        if all_are_equal and only_one:
            return i


summarized_p1 = 0
summarized_p2 = 0
for pattern in D:
    row_mirror = find_row_mirror(pattern)
    col_mirror = find_col_mirror(pattern)

    row_smudge_mirror = find_second_row_mirror(pattern)
    col_smudge_mirror = find_second_col_mirror(pattern)

    if row_mirror:
        summarized_p1 += 100 * row_mirror
    if col_mirror:
        summarized_p1 += col_mirror

    if row_smudge_mirror:
        summarized_p2 += 100 * row_smudge_mirror
    if col_smudge_mirror:
        summarized_p2 += col_smudge_mirror


print(summarized_p1)
print(summarized_p2)
