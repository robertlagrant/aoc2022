from dataclasses import dataclass, field

from inputs import TEST as commands

@dataclass
class Dir:
  name: str
  parent: "Dir" 
  children: list["Dir"] = field(default_factory=list)
  files: dict = field(default_factory=dict)

  @property
  def size(self):
    return sum(v for k, v in self.files.items()) + sum(c.size for c in self.children)

  @property
  def descendents(self):
    return self.children + [desc for c in self.children for desc in c.descendents]


def parse_dirs(command_list):
  root = Dir(name = "/", parent = None)
  current = root

  for command in map(lambda s: s.split(), command_list):
    match command:
      case ["$", "ls"]: continue
      case ["$", "cd", "/"]: current = root
      case ["$", "cd", ".."]: current = current.parent
      case ["$", "cd", new]: [c for c in current.children if c.name == new][0]
      case ["dir", filename]: current.children.append(Dir(name = filename, parent = current))
      case [size, filename]: current.files[filename] = int(size)

  return root

SPACE_REQUIRED = 70_000_000 - 30_000_000

root = parse_dirs(commands.split("\n"))

print(f"Part 1: {sum(d.size for d in root.descendents if d.size < 100000)}")
print(f"Part 2: {min(d.size for d in root.descendents if (root.size - SPACE_REQUIRED) <= d.size)}")
