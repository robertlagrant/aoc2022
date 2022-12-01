import re

from inputs import REAL #, TEST

elves = sorted(sum(map(int, re.split('\n', elf))) for elf in re.split('\n\n+', REAL))

print(f"Part 1: {elves[-1]}")
print(f"Part 2: {sum(elves[-3:])}")
