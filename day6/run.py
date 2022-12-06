from inputs import REAL as signal

def locate_start_packet(s, start_length):
    for i in range(1 + len(s) - start_length):
        if len(set(s[i:i + start_length])) == start_length:
            return i + start_length

print(f"Part 1: {locate_start_packet(signal, 4)}")
print(f"Part 2: {locate_start_packet(signal, 14)}")

