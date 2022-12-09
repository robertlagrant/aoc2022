from inputs import REAL as commands

directions = {
    "R": (1, 0), 
    "L": (-1, 0), 
    "U": (0, 1), 
    "D": (0, -1)
}

def steps(commands):
    for d, m in map(lambda s: s.split(), commands):
        for _ in range(int(m)):
            yield directions[d]


s = (0, 0)
Hs = [s]
Ts = [s] 

for i, (x_step, y_step) in enumerate(steps(commands.split("\n"))):
    T = Ts[-1]
    Hs.append(H := (Hs[-1][0] + x_step, Hs[-1][1] + y_step))

    x_diff = H[0] - T[0]
    y_diff = H[1] - T[1]
    if abs(x_diff) > 1 or abs(y_diff) > 1:
        tx_delta = -1 if x_diff < 0 else 1 if x_diff > 0 else 0
        ty_delta = -1 if y_diff < 0 else 1 if y_diff > 0 else 0
        Ts.append((T[0] + tx_delta, T[1] + ty_delta))
    else:
        Ts.append(T)

# x_min_print = min(s[0], *[h[0] for h in Hs], *[t[0] for t in Ts])
# y_min_print = min(s[1], *[h[1] for h in Hs], *[t[1] for t in Ts])
# x_max_print = max(s[0], *[h[0] for h in Hs], *[t[0] for t in Ts])
# y_max_print = max(s[1], *[h[1] for h in Hs], *[t[1] for t in Ts])

# for i in range(len(Hs)):    
#     print(f"({i})")
#     for y in range(y_max_print, y_min_print - 1, -1):
#         row = ""
#         for x in range(x_min_print, x_max_print + 1):
#             if (x, y) == Hs[i]:
#                 row += "H"
#             elif (x, y) == Ts[i]:
#                 row += "T"
#             elif (x, y) == s:
#                 row += "s"
#             else:
#                 row += "."
#         print(row)
    
#     print()

print(f"Part 1: {len(set(Ts))}")
