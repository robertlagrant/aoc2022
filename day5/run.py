from collections import defaultdict
import re

HEADER_PATTERN = r"(\d)"
BUCKET_PATTERN = r"([A-Z])"
INSTRUCTION_PATTERN = r"move (\d+) from (\d) to (\d)"

with open("input.txt") as f:
    lines = f.readlines()
    index_matches = re.finditer(HEADER_PATTERN, lines[0])

index_to_bucket = {i: lines[0][i] for i in [m.start(0) for m in index_matches]}
part_1_columns = defaultdict(list)
part_2_columns = defaultdict(list)

for line in lines[1:]:
    for index in map(lambda m: m.start(0), re.finditer(BUCKET_PATTERN, line)):
        part_1_columns[index_to_bucket[index]].append(line[index])
        part_2_columns[index_to_bucket[index]].append(line[index])

    if m := re.search(INSTRUCTION_PATTERN, line):
        count, source, dest = m.groups()
        for i in range(int(count)):
            part_1_columns[dest].insert(0, part_1_columns[source].pop(0))
            part_2_columns[dest].insert(0, part_2_columns[source].pop(int(count)-1-i))

print(f"Part 1: {''.join(v[0] for _, v in sorted(part_1_columns.items()))}")
print(f"Part 2: {''.join(v[0] for _, v in sorted(part_2_columns.items()))}")
