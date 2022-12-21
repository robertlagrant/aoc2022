from collections import deque

from inputs import REAL as data  

DECRYPTION_KEY = 811589153


def prepare_file(iterations=1, multiplier=1):
    file = deque()
    instructions = {}
    index_of_0 = None

    for i, instruction in enumerate(map(int, data.split("\n"))):
        instructions[i] = instruction * multiplier
        file.append((i))
        if instruction == 0:
          index_of_0 = i

    for _ in range(iterations):
      for i in range(len(file)):
          file.rotate(-file.index(i))
          file.popleft()
          file.rotate(-instructions[i])
          file.insert(0, i)
    
    return file, instructions, index_of_0


def sum_coordinates(file, instructions, index_of_0):
    i_index = file.index(index_of_0)
    file.rotate(-i_index)

    num = 0
    for _ in range(3):
      file.rotate(-1000)
      num += instructions[file[0]]

    return num


print(f"Part 1: {sum_coordinates(*prepare_file())}")
print(f"Part 2: {sum_coordinates(*prepare_file(iterations=10, multiplier=DECRYPTION_KEY))}")
