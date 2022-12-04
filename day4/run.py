import inputs

full_overlap_count = 0
partial_overlap_count = 0

for line in inputs.REAL.split("\n"):
  lhs, rhs = line.split(",")
  l_low, l_high = map(int, lhs.split("-"))
  r_low, r_high = map(int, rhs.split("-"))

  if l_low <= r_low and l_high >= r_high or r_low <= l_low and r_high >= l_high:
    full_overlap_count += 1

  if l_low <= r_low <= l_high or r_low <= l_low <= r_high:
    partial_overlap_count += 1

print(f"Part 1: {full_overlap_count}")
print(f"Part 2: {partial_overlap_count}")

