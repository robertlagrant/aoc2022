from inputs import REAL as signal

def locate_unique_sequence(s, length):
    return (j for i, j in enumerate(range(length, len(s))) if len(set(s[i:j])) == length)

print(f"Part 1: {next(locate_unique_sequence(signal, 4))}")
print(f"Part 2: {next(locate_unique_sequence(signal, 14))}")

