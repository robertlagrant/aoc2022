from itertools import pairwise

from inputs import REAL as data


def create_rock(data):
    rock = set()
    for path in data.split("\n"):
        for (l0, l1), (r0, r1) in pairwise([list(map(int, c.split(","))) for c in path.split(" -> ")]):
            if l0 == r0:
                for r in range(min(l1, r1), max(l1, r1) + 1):
                    rock.add((l0, r))
            else:
                for l in range(min(l0, r0), max(l0, r0) + 1):
                    rock.add((l, r1))
    
    return rock


def drop_sand(source, rock, sand, max_y, floor=None):
    x, y = source

    while (floor is None or y + 1 < floor) and (n_s := [s for xd, yd in [(0, 1), (-1, 1), (1, 1)] if (s := (x + xd, y + yd)) not in rock and s not in sand]):
        x, y = n_s[0]

        if floor is None and y > max_y:
            return None

    return x, y


def pour(source, rock, floor=None):
    sand = set()
    max_y = max(c[1] for c in {source} | rock) - 1
    while source not in sand and (new_sand := drop_sand(source, rock, sand, max_y, floor)):
        sand.add(new_sand)

    return sand


source = (500, 0)
rock = create_rock(data)
print(f"Part 1: {len(pour(source, rock))}")
print(f"Part 2: {len(pour(source, rock, floor=max(c[1] for c in {source} | rock) + 2))}")
