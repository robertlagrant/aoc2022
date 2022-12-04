import re

import inputs

MATCH = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")

nums = [(ll, lh, rl, rh) for ll, lh, rl, rh in [map(int, re.match(MATCH, l).groups()) for l in inputs.REAL.split("\n")]]

print(f"Part 1: {sum(ll <= rl and rh <= lh or rl <= ll and lh <= rh for ll, lh, rl, rh in nums)}")
print(f"Part 2: {sum(ll <= rl <= lh or rl <= ll <= rh for ll, lh, rl, rh in nums)}")

