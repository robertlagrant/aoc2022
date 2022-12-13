from inputs import REAL as data


def compare(left, right, num):
    match([left, right]):
        case [int(), int()]:
            print(f"{num} 1: {left, right}")
            return left <= right
        case [int(), list()]:
            print(f"{num} 2: {[left] * left, right}")
            return compare([left] * left, right, num)
        case [list(), int()]:
            print(f"{num} 3: {left, [right] * right}")
            return compare(left, [right] * right, num)
        case [list(), list()] if len(left) != len(right):
            print(f"{num} 4: {len(left)} {len(right)}")
            return len(left) <= len(right)
        case [list(), list()]:
            print(f"{num} 5: {left, right}")
            return all(compare(l, r, num) for l, r in zip(left, right))

for i, (left, right) in enumerate([map(eval, pair.split("\n")) for pair in data.split("\n\n")]):
    print(left)
    print(right)
    print(compare(left, right, i))
    print()


# print("Part 1:", sum(i + 1 for i, (l, r) in enumerate([map(eval, pair.split('\n')) for pair in data.split('\n\n')]) if compare(l, r, i)))
