from inputs import REAL as commands

S = (0, 0)
DIRECTIONS = {
    "R": (1, 0), 
    "L": (-1, 0), 
    "U": (0, 1), 
    "D": (0, -1)
}

def steps(commands):
    for d, m in map(lambda s: s.split(), commands):
        for _ in range(int(m)):
            yield DIRECTIONS[d]


class Knot:
    def __init__(self, name, parent=None):
        self.name = name
        self.child = None
        self.parent = parent
        if self.parent:
            self.parent.child = self
        self.pos = [S]


    def swaaaay(self, x_step=None, y_step=None):
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
            self.child.swaaaay()


def simulate_tail_positions(knots, commands):
    prev = root = Knot(name=knots[0])
    for c in knots[1:]:
        prev = Knot(name=c, parent=prev)

    for x_step, y_step in steps(commands.split("\n")):
        root.swaaaay(x_step, y_step)
    
    return prev.pos

print(f"Part 1: {len(set(simulate_tail_positions('HT', commands)))}")
print(f"Part 1: {len(set(simulate_tail_positions('H123456789', commands)))}")

# all_knots = [root]
# current = root
# while current.child:
#     all_knots.append(current.child)
#     current = current.child

# all_x = []
# all_y = []
# for k in all_knots:
#     for p in k.pos:
#         # print(k.name, p)
#         all_x.append(p[0])
#         all_y.append(p[1])
        

# x_min_print, x_max_print = min(all_x), max(all_x)
# y_min_print, y_max_print = min(all_y), max(all_y)

# for i in range(len(root.pos)):    
#     print(f"({i})")
#     for y in range(y_max_print, y_min_print - 1, -1):
#         row = ""
#         for x in range(x_min_print, x_max_print + 1):
#             if matches := [k.name for k in all_knots if (x, y) == k.pos[i]]:
#                 row += matches[0]
#             elif (x, y) == S:
#                 row += "s"
#             else:
#                 row += "."
#         print(row)
    
#     print()