import re

from inputs import REAL as data

MATCHER = re.compile(r"Sensor at x=(?P<sx>-?\d+), y=(?P<sy>-?\d+): closest beacon is at x=(?P<bx>-?\d+), y=(?P<by>-?\d+)")

TEST = {(-1,1), (0,2), (0,1), (0,0), (1,3), (1,2), (1,1), (1,0), (1,-1), (2,2), (2,1), (2,0), (3,1)}


def manhatten_dist(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


def manhatten_area_cuts(start, distance, row):
    covered = set()

    if start[1] == row:
        covered.update(range(start[0] - distance, 1 + start[0] + distance))
    elif start[1] < row < start[1] + distance:
        poke = distance - (row - start[1]) # 6
        covered.update(range(start[0] - poke, 1 + start[0] + poke)) # range(2, 15)
    elif start[1] - distance < row < start[1]:
        poke = distance - (start[1] - row)
        covered.update(range(start[0] - poke, 1 + start[0] + poke))

    return covered


def manhatten_area(start, distance):
    covered = {start}

    for i in range(1, distance + 1):
        covered.add((start[0], start[1] + i))
        covered.add((start[0], start[1] - i))
        covered.add((start[1] + i, start[1]))
        covered.add((start[1] - i, start[1]))
    
    for i in range(distance):
        for j in range(1, i + 1):
            covered.add((i + start[0] - distance, start[1] + j))
            covered.add((i + start[0] - distance, start[1] - j))

            covered.add((start[0] + distance - i, start[1] + j))
            covered.add((start[0] + distance - i, start[1] - j))

    return covered


if TEST - manhatten_area((1,1), 2):
    raise ValueError()

if manhatten_dist((1,1), (7, 1)) != 6:
    raise ValueError()

if manhatten_dist((5,2), (-4, 8)) != 15:
    raise ValueError()



# counter = 0
# for m in [{k: int(v) for k, v in MATCHER.match(d).groupdict().items()} for d in data.split("\n")]:
#     print((m["sx"], m["bx"]), (m["sy"], m["by"]))
#     beacons.add((m["bx"], m["by"]))
#     print(beacons)
#     distance = manhatten_dist((m["sx"], m["sy"]), (m["bx"], m["by"]))
#     print(distance)
#     covered.update(manhatten_area((m["sx"], m["sy"]), distance))

#     print (counter)
#     counter += 1

# print(len(c for c in covered if c[1] == 10 and c not in beacons))


row = 2000000
covered = set()
beacons = set()
for m in [{k: int(v) for k, v in MATCHER.match(d).groupdict().items()} for d in data.split("\n")]:
    beacon = (m["bx"], m["by"])
    sensor = (m["sx"], m["sy"])

    if m["by"] == row:
        beacons.add(beacon)
    
    distance = manhatten_dist(sensor, beacon)
    covered.update(manhatten_area_cuts(sensor, distance, row))
    
print(f"Part 1: {len(covered - set(y for _, y in beacons))}")


covered = set()
beacons = set()
for m in [{k: int(v) for k, v in MATCHER.match(d).groupdict().items()} for d in data.split("\n")]:
    beacon = (m["bx"], m["by"])
    sensor = (m["sx"], m["sy"])

    if m["by"] == row:
        beacons.add(beacon)
    
    distance = manhatten_dist(sensor, beacon)
    covered.update(manhatten_area_cuts(sensor, distance, row))

