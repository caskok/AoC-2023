lines = open('input/input11.txt', 'r').readlines()
D = [line.strip() for line in lines]

galaxies = []

cols = set()
rows = set()

for j in range(len(D)):
    for i in range(len(D[0])):
        if D[j][i] == '#':
            cols.add(i)
            rows.add(j)
            galaxies.append((i, j))

empty_rows = [row for row in range(len(D)) if row not in rows]
empty_cols = [col for col in range(len(D[0])) if col not in cols]

print(empty_rows)
print(empty_cols)
galaxies.sort()
print(galaxies)

distances = []
factor = 1000000
for idx, (x1, y1) in enumerate(galaxies):
    for (x2, y2) in galaxies[idx+1:]:
        extra_rows = len(list(filter(lambda a: a > min(y1, y2)
                                     and a < max(y1, y2), empty_rows)))
        extra_cols = len(list(filter(lambda a: a > min(x1, x2)
                                     and a < max(x1, x2), empty_cols)))
        x_dist = max(x2-x1, x1-x2)
        y_dist = max(y2-y1, y1-y2)
        distance = (x_dist
                    + y_dist
                    + (factor - 1) * extra_rows
                    + (factor - 1) * extra_cols)
        distances.append(distance)

print(sum(distances))
