from functools import reduce
from itertools import permutations, takewhile
from operator import mul

with open("input.txt") as f:
    trees = [list(map(int, line.strip())) for line in f.readlines()]
    side = len(trees)

low_trees = [
    (
        [trees[y][x] > trees[y][x1] for x1 in range(x - 1, -1, -1)],
        [trees[y][x] > trees[y][x1] for x1 in range(x + 1, side)],
        [trees[y][x] > trees[y1][x] for y1 in range(y - 1, -1, -1)],
        [trees[y][x] > trees[y1][x] for y1 in range(y + 1, side)],
    )
    for x, y in permutations(range(side), 2)
]

print(f"Part 1: {sum(not all(not all(d) for d in t) for t in low_trees)}")
print(f"Part 2: {max(reduce(mul, ((taken := sum(takewhile(bool, d))) + (taken < len(d)) for d in t)) for t in low_trees)}")
