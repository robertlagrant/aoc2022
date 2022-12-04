import re

import inputs

MATCH = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")

full_overlap_count = 0
partial_overlap_count = 0

for l_low, l_high, r_low, r_high in [map(int, re.match(MATCH, line).groups()) for line in inputs.REAL.split("\n")]:
  full_overlap_count += l_low <= r_low and r_high <= l_high or r_low <= l_low and l_high <= r_high
  partial_overlap_count += l_low <= r_low <= l_high or r_low <= l_low <= r_high

print(f"Part 1: {full_overlap_count}")
print(f"Part 2: {partial_overlap_count}")

