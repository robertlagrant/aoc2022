from inputs import TEST as tree_heights

trees = [list(map(int, t_row)) for t_row in tree_heights.split("\n")]
width = height = len(trees)

taller_trees = {
  (x, y): {
    "l": [trees[y][x] <= trees[y][x1] for x1 in range(0, x)],
    "r": [trees[y][x] <= trees[y][x1] for x1 in range(x+1, width)],
    "u": [trees[y][x] <= trees[y1][x] for y1 in range(0, y)],
    "d": [trees[y][x] <= trees[y1][x] for y1 in range(y+1, height)]
  } for x in range(width) for y in range(height)
}

print(f"Part 1: {sum(not all(any(taller_trees[(x,y)][d]) for d in 'lrud') for x in range(width) for y in range(height))}")

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
