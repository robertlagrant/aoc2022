import functools
import operator as op
import re

from inputs import REAL as DATA


class Monkey:
    inspection_count = 0
    monkey_parser = re.compile(
        r"""Monkey \d:
  Starting items: (?P<items>[\d, ]+)
  Operation: new = old (?P<op>[\+-/\*]) (?P<op_num>\d+|old)
  Test: divisible by (?P<test>\d+)
    If true: throw to monkey (?P<passed>\d)
    If false: throw to monkey (?P<failed>\d)"""
    )
    ops = {"+": op.add, "-": op.sub, "*": op.mul, "/": op.floordiv}

    def __init__(self, monkey_string):
        fields = self.monkey_parser.match(monkey_string).groupdict()
        self.items = list(map(int, fields["items"].split(", ")))
        self.op = self.ops[fields["op"]]
        self.op_num = int(fields["op_num"]) if fields["op_num"] != "old" else None  # None means use "old"
        self.test, self.passed, self.failed = map(int, [fields[f] for f in ("test", "passed", "failed")])

    def turn(self, monkeys, worry_divisor, lcm_optimisation):
        self.inspection_count += len(self.items)
        for item in self.items:
            item = self.op(item, item if self.op_num is None else self.op_num) // worry_divisor
            if lcm_optimisation:
                item %= lcm_optimisation
            monkeys[self.failed if item % self.test else self.passed].items.append(item)
        self.items = []


def sim_monkeys(worry_divisor, round_count):
    monkeys = {i: Monkey(m) for i, m in enumerate(DATA.split("\n\n"))}
    lcm = None if worry_divisor > 1 else functools.reduce(op.mul, [m.test for m in monkeys.values()])

    for _ in range(round_count):
        for i in range(len(monkeys)):
            monkeys[i].turn(monkeys, worry_divisor, lcm)

    return monkeys.values()


print(f"Part 1: {(counts := sorted(m.inspection_count for m in sim_monkeys(3, 20)))[-1] * counts[-2]}")
print(f"Part 2: {(counts := sorted(m.inspection_count for m in sim_monkeys(1, 10000)))[-1] * counts[-2]}")
