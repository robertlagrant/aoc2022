import functools
import operator as op
import re

from inputs import REAL as data


class Monkey:
    inspection_counter = 0
    monkey_parser = re.compile(
        r"""Monkey \d:
  Starting items: (?P<items>[\d, ]+)
  Operation: new = old (?P<op>[\+-/\*]) (?P<op_target>\d+|old)
  Test: divisible by (?P<test_div_by>\d+)
    If true: throw to monkey (?P<throw_to_pass>\d)
    If false: throw to monkey (?P<throw_to_fail>\d)"""
    )

    OPS = {"+": op.add, "-": op.sub, "*": op.mul, "/": op.floordiv}

    def __init__(self, monkey_string):
        fields = self.monkey_parser.match(monkey_string).groupdict()
        self.items = list(map(int, fields["items"].split(", ")))
        self.op = self.OPS[fields["op"]]
        self.op_target = int(fields["op_target"]) if fields["op_target"] != "old" else None  # None means use "old"
        self.test_div_by = int(fields["test_div_by"])
        self.throw_to_pass = int(fields["throw_to_pass"])
        self.throw_to_fail = int(fields["throw_to_fail"])

    def turn(self, monkeys, worry_divisor, lcm_optimisation=1):
        self.inspection_counter += len(self.items)
        for item in self.items:
            item = self.op(item, self.op_target if self.op_target is not None else item)  # worry operation
            item = item // worry_divisor % lcm_optimisation # boredom and lcm
            monkeys[self.throw_to_pass if item % self.test_div_by == 0 else self.throw_to_fail].items.append(item)
        self.items = []

def simulate_monkeys(worry_divisor, round_count):
    monkeys = {i: Monkey(m) for i, m in enumerate(data.split("\n\n"))}
    lcm = 1 if worry_divisor > 1 else functools.reduce(op.mul, [m.test_div_by for m in monkeys.values()])

    for _ in range(round_count):
        for i in range(len(monkeys)):
            monkeys[i].turn(monkeys, worry_divisor, lcm)

    return monkeys.values()


print(f"Part 1: {(counts := sorted(m.inspection_counter for m in  simulate_monkeys(3, 20)))[-1] * counts[-2]}")
print(f"Part 2: {(counts := sorted(m.inspection_counter for m in simulate_monkeys(1, 10000)))[-1] * counts[-2]}")
