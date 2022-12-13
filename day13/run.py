from inputs import REAL as data


def compare(left, right, num, depth=0):
    print(" "*depth*2 + f"- Compare {left} vs {right}")
    match([left, right]):
        case [int(), int()]:
            if left < right:
                print(" "*(1+depth)*2 + f"- Left side is smaller, so inputs are in the right order")
                return 1
            elif right < left:
                print(" "*(1+depth)*2 + f"- Right side is smaller, so inputs are not in the right order")
                return -1
            
            return 0
        case [int(), list()]:
            print(" "*(1+depth)*2 + f"- Mixed types; convert left to [{left}] and retry comparison")
            return compare([left], right, num, depth+1)
        case [list(), int()]:
            print(" "*(1+depth)*2 + f"- Mixed types; convert right to [{right}] and retry comparison")
            return compare(left, [right], num, depth+1)
        case [list(), list()]:
            for l, r in zip(left, right):
                result = compare(l, r, num, depth+1)
                if result != 0:
                    return result
            
            if len(left) < len(right):
                print(" "*(1+depth)*2 + f"- Left side ran out of items, so inputs are in the right order")
                return 1
            elif len(left) == len(right):
                return 0 
            
            print(" "*(1+depth)*2 + f"- Right side ran out of items, so inputs are not in the right order")
            return -1

for i, (left, right) in enumerate([map(eval, pair.split("\n")) for pair in data.split("\n\n")]):
    print(f"== Pair {i+1} ==")
    
    print(compare(left, right, i))


print("Part 1:", sum(i + 1 for i, (l, r) in enumerate([map(eval, pair.split('\n')) for pair in data.split('\n\n')]) if compare(l, r, i) in (0, 1)))
