from inputs import REAL as data


def compare(left, right):
    match([left, right]):
        case [int(), int()]:
            return 1 if left < right else -1 if right < left else 0
        case [int(), list()]:
            return compare([left], right)
        case [list(), int()]:
            return compare(left, [right])
        case [list(), list()]:
            for l, r in zip(left, right):
                result = compare(l, r)
                if result != 0:
                    return result
            
            return 1 if len(left) < len(right) else -1 if len(right) < len(left) else 0


print("Part 1:", sum(i + 1 for i, (l, r) in enumerate([map(eval, pair.split('\n')) for pair in data.split('\n\n')]) if compare(l, r) in (0, 1)))
