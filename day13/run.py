from functools import cmp_to_key
from itertools import chain
from math import prod

from inputs import REAL as data

DP = [[[2]], [[6]]] # divider packets


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
            
            return compare(len(left), len(right))


pairs = [list(map(eval, pair.split('\n'))) for pair in data.split('\n\n')]
print("Part 1:", sum(i + 1 for i, (l, r) in enumerate(pairs) if compare(l, r) != 1))
print("Part 2:", prod([i+1 for i, p in enumerate(sorted(chain.from_iterable(pairs + [DP]), key=cmp_to_key(compare))) if p in DP]))
