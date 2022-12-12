from typing import List, Tuple
from inputs import REAL as HM

def move_options(_x: int, _y: int, hm: List[List[str]]) -> List[Tuple[int, int]]:
    max_y, max_x = len(hm) - 1, len(hm[0]) - 1

    match(_x, _y):
        case [0, 0]:                              options = [(0, 1), (1, 0)]
        case [x, y] if x == max_x and y == max_y: options = [(x-1, y), (x, y-1)]
        case [0, y] if y == max_y:                options = [(0, y-1), (1, y)]  
        case [x, 0] if x == max_x:                options = [(x-1, 0), (x, 1)]   
        case [x, y] if y == max_y:                options = [(x-1, y), (x, y-1), (x+1, y)]
        case [x, y] if x == max_x:                options = [(x, y-1), (x-1, y), (x, y+1)]
        case [0, y]:                              options = [(0, y-1), (1, y), (0, y+1)]
        case [x, 0]:                              options = [(x-1, 0), (x, 1), (x+1, 0)]
        case [x, y]:                              options = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        case _:                                   raise ValueError()

    return [(x, y) for x, y in options if ord(hm[_y][_x]) - ord(hm[y][x]) >= -1] # check heights


hm = [list(l) for l in HM.split("\n")]
start = [(x, y) for y in range(len(hm)) for x in range(len(hm[0])) if hm[y][x] == "S"][0]
target = [(x, y) for y in range(len(hm)) for x in range(len(hm[0])) if hm[y][x] == "E"][0]
moves = {start: 0}

hm[start[1]][start[0]] = "a"
hm[target[1]][target[0]] = "z"

to_try = [start]
while to_try:
    current = to_try.pop(0)
    options = move_options(*current, hm)
    for o in options:
        if o in moves:
            if moves[current] + 1 < moves[o]:
                moves[o] = moves[current] + 1
        else:
            moves[o] = moves[current] + 1
            to_try.append(o)

print(f"Part 1: {moves[target]}")
