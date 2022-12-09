from inputs import REAL as commands

DIRECTIONS = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}


class Knot:
    def __init__(self, name, parent=None):
        self.name = name
        self.child = None
        if parent:
            parent.child = self
        self.pos = [(0, 0)]


    def swaaaay(self, x_step=None, y_step=None, parent=None):
        if parent is None:
            self.pos.append((self.pos[-1][0] + x_step, self.pos[-1][1] + y_step))
        else:
            x_diff = parent.pos[-1][0] - self.pos[-1][0]
            y_diff = parent.pos[-1][1] - self.pos[-1][1]
            if abs(x_diff) > 1 or abs(y_diff) > 1:
                tx_delta = -1 if x_diff < 0 else 1 if x_diff > 0 else 0
                ty_delta = -1 if y_diff < 0 else 1 if y_diff > 0 else 0
                self.pos.append((self.pos[-1][0] + tx_delta, self.pos[-1][1] + ty_delta))
            else:
                self.pos.append(self.pos[-1])

        if self.child:
            self.child.swaaaay(parent=self)


def simulate_tail_positions(knots, commands):
    last = first = Knot(name=knots[0])
    for c in knots[1:]:
        last = Knot(name=c, parent=last)

    for x_step, y_step in (DIRECTIONS[d] for d, m in (s.split() for s in commands) for _ in range(int(m))):
        first.swaaaay(x_step, y_step)

    return last.pos


print(f"Part 1: {len(set(simulate_tail_positions('HT', commands.splitlines())))}")
print(f"Part 1: {len(set(simulate_tail_positions('H123456789', commands.splitlines())))}")
