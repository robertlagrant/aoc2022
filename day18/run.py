from inputs import REAL as data

MANHATTAN_3D = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))

CUBES = set(tuple(map(int, line.split(","))) for line in data.split("\n"))


def face_count(c, cubes):
    return sum((c[0] + xd, c[1] + yd, c[2] + zd) not in cubes for xd, yd, zd in MANHATTAN_3D)


def face_count_in_steam(c, steam):
    return sum((c[0] + xd, c[1] + yd, c[2] + zd) in steam for xd, yd, zd in MANHATTAN_3D)


def fill_with_steam(cubes):
    cubes_list = list(cubes)
    xm, ym, zm = cubes_list[0]
    xx, yx, zx = cubes_list[0]

    for c in cubes_list[1:]:
        xm, xx = min(xm, c[0]), max(xx, c[0])
        ym, yx = min(ym, c[1]), max(yx, c[1])
        zm, zx = min(zm, c[2]), max(zx, c[2])

    steam = set()
    candidate_steam = [(xm - 1, ym - 1, zm - 1)]
    while candidate_steam:
        s = candidate_steam.pop()
        steam.add(s)
        for dx, dy, dz in MANHATTAN_3D:
            m = s[0] + dx, s[1] + dy, s[2] + dz
            if (xm - 1) <= m[0] <= (xx + 1) and (ym - 1) <= m[1] <= (yx + 1) and (zm - 1) <= m[2] <= (zx + 1):
                if m not in steam and m not in cubes:
                    candidate_steam.append(m)
    
    return steam


steam = fill_with_steam(CUBES)
print(f"Part 1: {sum(face_count(c, CUBES) for c in CUBES)}") 
print(f"Part 2: {sum(face_count_in_steam(c, steam) for c in CUBES)}")
