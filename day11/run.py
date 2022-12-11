import operator as op
import re

from inputs import REAL as data


class Monkey:
    PARSE_MONKEY = r"""Monkey \d:
  Starting items: (?P<items>[\d, ]+)
  Operation: new = old (?P<op>[\+-/\*]) (?P<op_target>\d+|old)
  Test: divisible by (?P<test_div_by>\d+)
    If true: throw to monkey (?P<test_pass_throw_to>\d)
    If false: throw to monkey (?P<test_fail_throw_to>\d)"""

    OPS = {"+": op.add, "-": op.sub, "*": op.mul, "/": op.floordiv}

    def __init__(self, monkey_string, worry_divisor):
        fields = re.match(self.PARSE_MONKEY, monkey_string).groupdict()
        self.items = list(map(int, fields['items'].split(", ")))
        self.op = self.OPS[fields["op"]]
        self.op_target = int(fields["op_target"]) if fields["op_target"] != "old" else None # None means use "old" as a target
        self.worry_divisor = worry_divisor
        self.test_div_by = int(fields["test_div_by"])
        self.test_pass_throw_to = int(fields["test_pass_throw_to"])
        self.test_fail_throw_to = int(fields["test_fail_throw_to"])
        self.item_inspection_counter = 0
    
    def turn(self, monkeys):
        while self.items:
            self.item_inspection_counter += 1
            item = self.items.pop(0)
            item = self.op(item, self.op_target if self.op_target else item) # worry operation
            item = item // self.worry_divisor # boredom
            next_monkey = self.test_pass_throw_to if item % self.test_div_by == 0 else self.test_fail_throw_to
            monkeys[next_monkey].items.append(item)

    def __repr__(self):
        return f"{self.items} {self.op} {self.op_target} {self.test_div_by} {self.test_pass_throw_to} {self.test_fail_throw_to}"



def simulate_monkey_inspection_counts(worry_divisor, round_count):
    monkeys = {i: Monkey(m, worry_divisor) for i, m in enumerate(data.split("\n\n"))}

    for round in range(round_count):
        print(round)
        for i in range(len(monkeys)):
            monkeys[i].turn(monkeys)
        
        # print(f"After round {round+1}, the monkeys are holding items with these worry levels:")
        # for i in range(len(monkeys)):
        #     print(f"Monkey {i}: {monkeys[i].items}")

    return sorted(m.item_inspection_counter for m in monkeys.values())


print(f"Part 1: {(counts := simulate_monkey_inspection_counts(3, 20))[-1] * counts[-2]}")
print(f"Part 2: {(counts := simulate_monkey_inspection_counts(1, 10000))[-1] * counts[-2]}")