from functools import reduce
import string

import inputs

PRIORITIES = {l: i+1 for i, l in enumerate(string.ascii_lowercase + string.ascii_uppercase)}

def common_score(*ins):
  return PRIORITIES[next(iter(reduce(lambda x, y: set(x) & set(y), ins)))]

lines = inputs.REAL.split('\n')
print(f"Part 1: {sum(common_score(line[:(halfway := len(line)//2)], line[halfway:]) for line in lines)}")
print(f"Part 2: {sum(common_score(*lines[i:i+3]) for i in range(0, len(lines), 3))}")
