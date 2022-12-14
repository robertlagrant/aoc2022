from itertools import pairwise

from inputs import REAL as data


def pprint(source, rock, sand):
    lines = []
    for y in range(min(c[1] for c in source | rock | sand), max(c[1] for c in source | rock | sand) + 1):
        line = ""
        for x in range(min(c[0] for c in source | rock | sand), max(c[0] for c in source | rock | sand) + 1):
            line += "#" if (x, y) in rock else "o" if (x, y) in sand else "+" if (x, y) in source else "."
        lines.append(line)

    print("\n".join(lines))


source = (500, 0)
rock = set()
sand = set()

for path in data.split("\n"):
    coordinates = [list(map(int, c.split(","))) for c in path.split(" -> ")]
    for (l0, l1), (r0, r1) in pairwise(coordinates):
        if l0 == r0:
            for r in range(min(l1, r1), max(l1, r1) + 1):
                rock.add((l0, r))
        else:
            for l in range(min(l0, r0), max(l0, r0) + 1):
                rock.add((l, r1))




def drop_sand(source, rock, sand, use_floor=False):
    max_y = max(c[1] for c in {source} | rock | sand) - 1
    current_x, current_y = source
    while True:
        if not use_floor and current_y > max_y:
            return None
        elif (current_x, current_y + 1) not in rock | sand:
            current_y += 1
        elif (current_x - 1, current_y + 1) not in rock | sand:
            current_x -= 1
            current_y += 1
        elif (current_x + 1, current_y + 1) not in rock | sand:
            current_x += 1
            current_y += 1
        else:
            break
    
    return sand | set([(current_x, current_y)])

counter = 0
# pprint({source}, rock, sand)
while True:
    # print(counter)
    # pprint(({source}, rock, sand))
    # print()
    new_sand = drop_sand(source, rock, sand)
    if new_sand:
        sand = new_sand
        counter += 1
    else:
        break

print(f"Part 1: {counter}")
