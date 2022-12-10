from inputs import TEST as commands

KEY_CYCLES = (20, 60, 100, 140, 180, 220)
X = 1

adds = {} 

for cycle, command in enumerate(commands.splitlines()):
  OLD_X = X

  match(command.split()):
    case ["addx", num]: 
      adds[cycle+2] = num
    case ["noop"]: ...

  # print(adds)
  if cycle in adds:
    X = X + int(adds[cycle])
    del adds[cycle]

  print(f"Cycle index {cycle} {OLD_X} -> {X} || {adds}")
  # if cycle + 1 in KEY_CYCLES:
  #   print(cycle + 1, X)
