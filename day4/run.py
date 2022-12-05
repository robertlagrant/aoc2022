import re

with open("input.txt") as f:
    nums = [list(map(int, re.split("[,-]", l))) for l in f.readlines()]

print(f"Part 1: {sum(l1 <= r1 and r2 <= l2 or r1 <= l1 and l2 <= r2 for l1, l2, r1, r2 in nums)}")
print(f"Part 2: {sum(l1 <= r1 <= l2 or r1 <= l1 <= r2 for l1, l2, r1, r2 in nums)}")
