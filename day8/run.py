from functools import reduce
from itertools import permutations, takewhile
from operator import mul

from inputs import REAL as tree_heights

trees = [list(map(int, t_row)) for t_row in tree_heights.split("\n")]
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
