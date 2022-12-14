from itertools import pairwise

from inputs import TEST as data

source = set([(500, 0)])
rock = set()
sand = set()

def draw(source, rock, sand):
    lines = []
    for y in range(min(c[1] for c in source | rock | sand), max(c[1] for c in source | rock | sand) + 1):
        line = ""
        for x in range(min(c[0] for c in source | rock | sand), max(c[0] for c in source | rock | sand) + 1):
            line += "#" if (x, y) in rock else "o" if (x, y) in sand else "+" if (x, y) in source else "."
        lines.append(line)

    return lines


for path in data.split("\n"):
    coordinates = [list(map(int, c.split(","))) for c in path.split(" -> ")]
    for (l0, l1), (r0, r1) in pairwise(coordinates):
        if l0 == r0:
            for r in range(min(l1, r1), max(l1, r1)+1):
                rock.add((l0, r))
        else:
            for l in range(min(l0, r0), max(l0, r0)+1):
                    rock.add((l, r1))


print("\n".join(draw(source, rock, sand)))