from functools import reduce
from itertools import takewhile
from operator import mul

from inputs import REAL as tree_heights

trees = [list(map(int, t_row)) for t_row in tree_heights.split("\n")]
width = height = len(trees)

taller_trees = {
  (x, y): {
    "l": [trees[y][x] <= trees[y][x1] for x1 in range(x-1, -1, -1)],
    "r": [trees[y][x] <= trees[y][x1] for x1 in range(x+1, width)],
    "u": [trees[y][x] <= trees[y1][x] for y1 in range(y-1, -1, -1)],
    "d": [trees[y][x] <= trees[y1][x] for y1 in range(y+1, height)]
  } for x in range(width) for y in range(height)
}

print(f"Part 1: {sum(not all(any(taller_trees[(x,y)][d]) for d in 'lrud') for x in range(width) for y in range(height))}")
print(f"Part 2: {max(reduce(mul, ((taken := sum(not n for n in takewhile(lambda x: not x, tt_d))) + (taken < len(tt_d)) for tt_d in [taller_trees[(x, y)][d] for d in 'lrud'])) for x in range(width) for y in range(height))}")
