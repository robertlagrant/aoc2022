import string

import inputs

PRIORITIES = {l: i+1 for i, l in enumerate(string.ascii_lowercase + string.ascii_uppercase)}

total_1 = 0
total_2 = 0

lines = inputs.REAL.split('\n')

for line in lines:
  half = len(line) // 2
  common = next(iter(set(line[:half]) & set(line[half:])))
  total_1 += PRIORITIES[common]

for i in range(0, len(lines), 3):
  common = next(iter(set(lines[i]) & set(lines[i+1]) & set(lines[i+2])))
  total_2 += PRIORITIES[common]

print(f"Part 1: {total_1}")
print(f"Part 1: {total_2}")