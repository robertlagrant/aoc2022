from inputs import REAL as commands

KEY_CYCLES = (20, 60, 100, 140, 180, 220)
SCREEN_WIDTH = 40
SCREEN_HEIGHT = 6
X = 1

cycle = 0
key_cycles_sum = 0
pixels = ""

def do_stuff(cycle, pixels, key_cycles_sum):
    pixels += "#" if cycle % 40 in (X - 1, X, X + 1) else "."
    cycle += 1
    if cycle in KEY_CYCLES:
        key_cycles_sum += cycle * X
    
    return cycle, pixels, key_cycles_sum


for command in commands.splitlines():
  cycle, pixels, key_cycles_sum = do_stuff(cycle, pixels, key_cycles_sum)
  
  match(command.split()):
    case ["addx", num]: 
      cycle, pixels, key_cycles_sum = do_stuff(cycle, pixels, key_cycles_sum)
      X += int(num)

print(f"Part 1: {key_cycles_sum}")
for i in range(0, SCREEN_WIDTH * SCREEN_HEIGHT, SCREEN_WIDTH):
  print(f"Part 2: {pixels[i:i+40]}")