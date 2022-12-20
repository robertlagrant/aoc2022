from itertools import combinations_with_replacement 

from inputs import REAL as data

points = set(tuple(map(int, line.split(","))) for line in data.split("\n"))
    

def face_count(p, points):
    return sum((p[0] + xd, p[1] + yd, p[2] + zd) not in points for xd, yd, zd in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)))


print(f"Part 1: {sum(face_count(p, points) for p in points)}") 
