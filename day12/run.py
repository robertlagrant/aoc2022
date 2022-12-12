from itertools import chain, product
from typing import Dict, List, Tuple

from inputs import REAL as HM


def move_options(_x: int, _y: int, hm: List[List[str]]) -> List[Tuple[int, int]]:
    max_y, max_x = len(hm) - 1, len(hm[0]) - 1

    match (_x, _y):
        case [0, 0]:                              options = [(0, 1), (1, 0)]
        case [x, y] if x == max_x and y == max_y: options = [(x - 1, y), (x, y - 1)]
        case [0, y] if y == max_y:                options = [(0, y - 1), (1, y)]
        case [x, 0] if x == max_x:                options = [(x - 1, 0), (x, 1)]
        case [x, y] if y == max_y:                options = [(x - 1, y), (x, y - 1), (x + 1, y)]
        case [x, y] if x == max_x:                options = [(x, y - 1), (x - 1, y), (x, y + 1)]
        case [0, y]:                              options = [(0, y - 1), (1, y), (0, y + 1)]
        case [x, 0]:                              options = [(x - 1, 0), (x, 1), (x + 1, 0)]
        case [x, y]:                              options = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

    return [(x, y) for x, y in options if ord(hm[_y][_x]) - ord(hm[y][x]) >= -1]  # check heights


def random_walk(hm: List[List[str]], start: Tuple[int, int]) -> Dict[Tuple[int, int], int]:
    moves, to_try = {start: 0}, [start]

    while to_try:
        current = to_try.pop(0)
        for o in move_options(*current, hm):
            if o in moves:
                if moves[current] + 1 < moves[o]:
                    moves[o] = moves[current] + 1
            else:
                moves[o] = moves[current] + 1
                to_try.append(o)

    return moves


def find_and_replace(hm, c1, c2):
    found = [(x, y) for y in range(len(hm)) for x in range(len(hm[0])) if hm[y][x] == c1][0]
    hm[found[1]][found[0]] = c2

    return hm, found


hm = [list(l) for l in HM.split("\n")]
hm, target = find_and_replace(hm, "E", "z") # Find target and turn into a z
hm, start_s = find_and_replace(hm, "S", "a") # Find start and turn into a a
edge = chain(product(range(len(hm[0])), (0, len(hm) - 1)), product((0, len(hm[0]) - 1), range(len(hm)))) # Get the edge

print(f"Part 1: {random_walk(hm, start_s)[target]}")
print(f"Part 2: {min(moves[target] for x, y in edge if hm[y][x] == 'a' and target in (moves := random_walk(hm, (x, y))))}")
