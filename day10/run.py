from inputs import REAL as commands

KEY_CYCLES = (20, 60, 100, 140, 180, 220)
SCREEN_WIDTH = 40
SCREEN_HEIGHT = 6
X = 1

def cycle(commands):
  cycle, x  = 0, 1
  for command in commands.splitlines():
    yield (cycle, x)
    cycle += 1
    if command.startswith("addx"):
      yield (cycle, x)
      cycle += 1
      x += int(command.split()[1])


print(f"Part 1: {sum((cycle + 1) * x for cycle, x in cycle(commands) if cycle + 1 in KEY_CYCLES)}")

pixels = "".join(["#" if cycle % 40 in (x - 1, x, x + 1) else "." for cycle, x in cycle(commands)])
for i in range(0, SCREEN_WIDTH * SCREEN_HEIGHT, SCREEN_WIDTH):
  print(f"Part 2: {pixels[i:i + SCREEN_WIDTH]}")
