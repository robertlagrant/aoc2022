from dataclasses import dataclass, field

from inputs import REAL as commands

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
  root_dir = Dir(name = "/", parent = None)
  current_dir = root_dir

  for line in command_list:
    if line.startswith("$ ls"):
      continue 
    elif line.startswith("$ cd"):
      new_dir = line.split()[-1]
      if new_dir == "..":
        current_dir = current_dir.parent
      else:
        for d in current_dir.children:
          if d.name == new_dir:
            current_dir = d
            break
    else:
      size_or_dir, filename = line.split()
      if size_or_dir == "dir":
        current_dir.children.append(Dir(name = filename, parent = current_dir))
      else:
        current_dir.files[filename] = int(size_or_dir)

  return root_dir

SPACE_REQUIRED = 70_000_000 - 30_000_000

root = parse_dirs(commands.split("\n"))

print(f"Part 1: {sum(d.size for d in root.descendents if d.size < 100000)}")
print(f"Part 2: {min(d.size for d in root.descendents if (root.size - SPACE_REQUIRED) <= d.size)}")
