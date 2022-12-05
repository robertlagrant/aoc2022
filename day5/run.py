from collections import defaultdict
import re

HEAD_PATTERN = r"(\d)"
BUCKET_PATTERN = r"([A-Z])"
INSTRUCTION_PATTERN = r"move (\d+) from (\d) to (\d)"

with open("input.txt") as f:
    head, rest = f.read().split("\n", 1)
    bucket_lines, move_lines = rest.split("\n\n")

index_to_bucket = {i: head[i] for i in [m.start(0) for m in re.finditer(HEAD_PATTERN, head)]}
part_1_columns = defaultdict(list)
part_2_columns = defaultdict(list)

for line in bucket_lines.split("\n"):
    for index in map(lambda m: m.start(0), re.finditer(BUCKET_PATTERN, line)):
        part_1_columns[index_to_bucket[index]].append(line[index])
        part_2_columns[index_to_bucket[index]].append(line[index])

for line in move_lines.split("\n"):
    count, source, dest = re.search(INSTRUCTION_PATTERN, line).groups()
    for i in range(int(count)):
        part_1_columns[dest].insert(0, part_1_columns[source].pop(0))
        part_2_columns[dest].insert(0, part_2_columns[source].pop(int(count)-1-i))

print(f"Part 1: {''.join(v[0] for _, v in sorted(part_1_columns.items()))}")
print(f"Part 2: {''.join(v[0] for _, v in sorted(part_2_columns.items()))}")
