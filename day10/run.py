from inputs import REAL as commands

KEY_CYCLES = (20, 60, 100, 140, 180, 220)
SCREEN_WIDTH = 40
SCREEN_HEIGHT = 6


def cycle(commands):
    x = 1
    for command in commands.splitlines():
        yield x
        if command.startswith("addx"):
            yield x
            x += int(command.split()[1])


print(f"Part 1: {sum((c + 1) * x for c, x in enumerate(cycle(commands)) if c + 1 in KEY_CYCLES)}")

pixels = "".join(["#" if c % 40 in (x - 1, x, x + 1) else "." for c, x in enumerate(cycle(commands))])
for i in range(0, SCREEN_WIDTH * SCREEN_HEIGHT, SCREEN_WIDTH):
    print(f"Part 2: {pixels[i:i + SCREEN_WIDTH]}")