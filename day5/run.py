import re
from collections import defaultdict

BUCKET_PATTERN = r"([A-Z])"
INSTRUCTION_PATTERN = r"move (\d+) from (\d) to (\d)"

COLUMN_INDEX_TO_BUCKET = {}
COLUMNS = defaultdict(list)

with open("input.txt") as f:
    lines = f.readlines()
    index_matches = re.finditer(r"(\d)", lines[0])

for index in [match.start(0) for match in index_matches]:
    COLUMN_INDEX_TO_BUCKET[index] = lines[0][index] 

for line in lines[1:]:
  if re.search(BUCKET_PATTERN, line):
    bucket_match = re.finditer(BUCKET_PATTERN, line)
    for m in bucket_match:
      COLUMNS[COLUMN_INDEX_TO_BUCKET[m.start(0)]].append(line[m.start(0)])

  if m := re.search(INSTRUCTION_PATTERN, line):
    count, source, dest = m.groups()
    for i in range(int(count)):
      # COLUMNS[dest].insert(0, COLUMNS[source].pop(0)) - part 1
      COLUMNS[dest].insert(0, COLUMNS[source].pop(int(count)-1-i))


print(COLUMNS)

print("".join(COLUMNS[column][0] for column in sorted(COLUMNS.keys())))


