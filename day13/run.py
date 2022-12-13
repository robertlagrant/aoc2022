from functools import cmp_to_key
from itertools import chain
from math import prod

from inputs import REAL as data

DIVIDERS = [[[2]], [[6]]]


def compare(left, right):
    match([left, right]):
        case [int(), int()]:
            return -1 if left < right else 1 if right < left else 0
        case [int(), list()]:
            return compare([left], right)
        case [list(), int()]:
            return compare(left, [right])
        case [list(), list()]:
            for l, r in zip(left, right):
                if (result := compare(l, r)) != 0:
                    return result
            
            return -1 if len(left) < len(right) else 1 if len(right) < len(left) else 0


pairs = [list(map(eval, pair.split('\n'))) for pair in data.split('\n\n')]
print("Part 1:", sum(i + 1 for i, (l, r) in enumerate(pairs) if compare(l, r) != 1))
print("Part 2:", prod([i+1 for i, x in enumerate(sorted(chain.from_iterable(pairs + [DIVIDERS]), key=cmp_to_key(compare))) if x in DIVIDERS]))
