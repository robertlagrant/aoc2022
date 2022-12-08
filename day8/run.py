from itertools import product

from inputs import REAL as tree_map

trees = [list(map(int, t_row)) for t_row in tree_map.split("\n")]
width = len(trees[0])
height = len(trees)
count = 0
for x, y in product(range(width), range(height)):
  x_left = any(1 for x1 in range(0, x) if trees[x][y] <= trees[x1][y])
  x_right = any(1 for x1 in range(x+1, width) if trees[x][y] <= trees[x1][y])
  y_up = any(1 for y1 in range(0, y) if trees[x][y] <= trees[x][y1])
  y_down = any(1 for y1 in range(y+1, height) if trees[x][y] <= trees[x][y1])

  if not (x_left and x_right and y_up and y_down):
    count += 1 


print(f"Part 1: {count}")

best_scenic_score = None
for x, y in product(range(width), range(height)):
  x_left_count = 0
  for x1 in range(x-1, -1, -1):
    x_left_count += 1
    if trees[x][y] <= trees[x1][y]:
      break

  x_right_count = 0
  for x1 in range(x+1, width):
    x_right_count += 1
    if trees[x][y] <= trees[x1][y]:
      break

  y_up_count = 0
  for y1 in range(y-1, -1, -1):
    y_up_count += 1
    if trees[x][y] <= trees[x][y1]:
      break

  y_down_count = 0
  for y1 in range(y+1, height):
    y_down_count += 1
    if trees[x][y] <= trees[x][y1]:
      break
  
  scenic_score = x_left_count * x_right_count * y_up_count * y_down_count
  if best_scenic_score is None or best_scenic_score < scenic_score:
    best_scenic_score = scenic_score

print(f"Part 2: {best_scenic_score}")
