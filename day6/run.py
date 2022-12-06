import inputs

def locate_start_packet(s, start_length):
    for i in range(len(s) - start_length - 1):
        if len(set(s[i:i + start_length])) == start_length:
            return i + start_length

print(f"Part 1: {locate_start_packet(inputs.REAL, 4)}")
print(f"Part 2: {locate_start_packet(inputs.REAL, 14)}")

