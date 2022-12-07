from dataclasses import dataclass, field

from inputs import TEST as commands

TOTAL_SPACE = 70000000
NEEDED_SPACE = 30000000

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
  def recurse_children(self):
    dirs = [d for d in self.children]
    while dirs:
      d = dirs.pop()
      dirs.extend(d.children)
      yield d


def parse_dirs():
  root_dir = Dir(name = "/", parent = None)
  current_dir = root_dir

  for line in commands.split("\n"):
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


root = parse_dirs()

print(f"Part 1: {sum(d.size for d in root.recurse_children if d.size < 100000)}")
print(f"Part 2: {min(d.size for d in root.recurse_children if (root.size - (TOTAL_SPACE - NEEDED_SPACE)) <= d.size)}")
