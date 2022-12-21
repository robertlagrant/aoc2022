from inputs import REAL as data

MANHATTAN_3D = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))

CUBES = set(tuple(map(int, line.split(","))) for line in data.split("\n"))


def face_count(c, cubes):
    return sum((c[0] + xd, c[1] + yd, c[2] + zd) not in cubes for xd, yd, zd in MANHATTAN_3D)


def face_count_in_steam(c, steam):
    return sum((c[0] + xd, c[1] + yd, c[2] + zd) in steam for xd, yd, zd in MANHATTAN_3D)


def fill_with_steam(cubes):
    cubes_list = list(cubes)
    x_min, y_min, z_min = cubes_list[0]
    x_max, y_max, z_max = cubes_list[0]

    for c in cubes_list[1:]:
        x_min, x_max = min(x_min, c[0]), max(x_max, c[0])
        y_min, y_max = min(y_min, c[1]), max(y_max, c[1])
        z_min, z_max = min(z_min, c[2]), max(z_max, c[2])

    steam = set()
    cubes_touching_steam = set()

    candidate_steam = [(x_min - 1, y_min - 1, z_min - 1)]
    while candidate_steam:
        s = candidate_steam.pop()
        if s not in steam:
            steam.add(s)
            for dx, dy, dz in MANHATTAN_3D:
                m = s[0] + dx, s[1] + dy, s[2] + dz
                if (x_min - 1) <= m[0] <= (x_max + 1) and (y_min - 1) <= m[1] <= (y_max + 1) and (z_min - 1) <= m[2] <= (z_max + 1):
                    if m in cubes:
                        cubes_touching_steam.add(m)
                    if m not in steam and m not in cubes:
                        candidate_steam.append(m)
    
    return cubes_touching_steam, steam

cubes_touching_steam, steam = fill_with_steam(CUBES)

print(f"Part 1: {sum(face_count(c, CUBES) for c in CUBES)}") 
print(f"Part 2: {sum(face_count_in_steam(c, steam) for c in cubes_touching_steam)}")
