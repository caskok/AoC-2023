lines = open('input/input9.txt', 'r').readlines()
D = [line.strip().split() for line in lines]
D = [[int(x) for x in line] for line in D]


def part1(history: list[int]):
    diffs = [history]

    for depth in range(len(history) - 1):
        diff = []
        for i, j in zip(diffs[depth], diffs[depth][1:]):
            diff.append(j-i)

        diffs.append(diff)

        # Check if all differences all 0, so we can stop.
        if not any(diff):
            break
    return sum([line[-1] for line in diffs])


def part2(history: list[int]):
    diffs = [history]

    for depth in range(len(history) - 1):
        diff = []
        for i, j in zip(diffs[depth], diffs[depth][1:]):
            diff.append(j-i)

        diffs.append(diff)

        # Check if all differences all 0, so we can stop.
        if not any(diff):
            break
    first_elements = [line[0] for line in diffs]
    positives = [item for index, item in enumerate(first_elements)
                 if not index % 2]
    negatives = [-item for index, item in enumerate(first_elements)
                 if index % 2]
    return sum(negatives) + sum(positives)


p1 = 0
p2 = 0
for line in D:
    p1 += part1(line)
    p2 += part2(line)

print(p1)
print(p2)
