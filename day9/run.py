from inputs import REAL as commands

directions = {
    "R": (1, 0), 
    "L": (-1, 0), 
    "U": (0, 1), 
    "D": (0, -1)
}

def steps(commands):
    for d, m in map(lambda s: s.split(), commands):
        for _ in range(int(m)):
            yield directions[d]


S = (0, 0)

class Knot:
    def __init__(self, name, parent=None):
        self.name = name
        self.child = None
        self.parent = parent
        if self.parent:
            self.parent.child = self
        self.pos = [S]


    def go(self, x_step=None, y_step=None):
        if self.parent is None:
            self.pos.append((self.pos[-1][0] + x_step, self.pos[-1][1] + y_step))
        else:
            x_diff = self.parent.pos[-1][0] - self.pos[-1][0]
            y_diff = self.parent.pos[-1][1] - self.pos[-1][1]
            if abs(x_diff) > 1 or abs(y_diff) > 1:
                tx_delta = -1 if x_diff < 0 else 1 if x_diff > 0 else 0
                ty_delta = -1 if y_diff < 0 else 1 if y_diff > 0 else 0
                self.pos.append((self.pos[-1][0] + tx_delta, self.pos[-1][1] + ty_delta))
            else:
                self.pos.append(self.pos[-1])
            
        if self.child:
            self.child.go()
        
    def __repr__(self):
        return f"{self.name} {self.pos} {self.parent.name if self.parent else 'no parent'}"

prev = root = Knot(name="H")
for c in "T":
    prev = Knot(name=c, parent=prev)

for i, (x_step, y_step) in enumerate(steps(commands.split("\n"))):
    root.go(x_step, y_step)

# x_min_print = min(S[0], *[h[0] for h in root.pos], *[t[0] for t in prev.pos])
# y_min_print = min(S[1], *[h[1] for h in root.pos], *[t[1] for t in prev.pos])
# x_max_print = max(S[0], *[h[0] for h in root.pos], *[t[0] for t in prev.pos])
# y_max_print = max(S[1], *[h[1] for h in root.pos], *[t[1] for t in prev.pos])

# for i in range(len(root.pos)):    
#     # print(f"({i})")
#     for y in range(y_max_print, y_min_print - 1, -1):
#         row = ""
#         for x in range(x_min_print, x_max_print + 1):
#             if (x, y) == root.pos[i]:
#                 row += "H"
#             elif (x, y) == prev.pos[i]:
#                 row += "T"
#             elif (x, y) == S:
#                 row += "s"
#             else:
#                 row += "."
#         print(row)
    
#     print()

print(f"Part 1: {len(set(prev.pos))}")

