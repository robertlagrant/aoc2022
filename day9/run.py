from inputs import REAL as commands

D = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}


class Knot:
    def __init__(self, knots):
        self.name = knots[0]
        self.pos_history = [(0, 0)]
        self.child = Knot(knots[1:]) if knots[1:] else None

    @property
    def pos(self):
        return self.pos_history[-1]

    def step(self, s=(0, 0)):
        self.pos_history.append((self.pos[0] + s[0], self.pos[1] + s[1]))

    def swaay(self, step=None, parent=None):
        if step:
            self.step(step)
        else:
            ds = parent.pos[0] - self.pos[0], parent.pos[1] - self.pos[1]
            self.step([0 if all(abs(d) <= 1 for d in ds) else -1 if d < 0 else 1 if d > 0 else 0 for d in ds])

        return [self.pos] + (self.child.swaay(parent=self) if self.child else [])


def simulate_tail_positions(knots, commands):
    return [knots.swaay(D[d])[-1] for d in [d for d, m in (s.split() for s in commands) for _ in range(int(m))]]


print(f"Part 1: {len(set(simulate_tail_positions(Knot('HT'), commands.splitlines())))}")
print(f"Part 2: {len(set(simulate_tail_positions(Knot('H123456789'), commands.splitlines())))}")
