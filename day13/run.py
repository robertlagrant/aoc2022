from functools import cmp_to_key
from itertools import chain
from math import prod

from inputs import REAL as data

DP = [[[2]], [[6]]]  # divider packets


def comp(left, right):
    match ([left, right]):
        case [int(), int()]:
            return -1 if left < right else 1 if right < left else 0
        case [int(), list()]:
            return comp([left], right)
        case [list(), int()]:
            return comp(left, [right])
        case [list(), list()]:
            return next(iter([res for l, r in zip(left, right) if (res := comp(l, r))]), comp(len(left), len(right)))


pairs = [list(map(eval, pair.split("\n"))) for pair in data.split("\n\n")]
print("Part 1:", sum(i + 1 for i, (l, r) in enumerate(pairs) if comp(l, r) != 1))
print("Part 2:", prod([i + 1 for i, p in enumerate(sorted(chain.from_iterable(pairs + [DP]), key=cmp_to_key(comp))) if p in DP]))
