import inputs

SYNONYMS = {
  "X": "ROCK",
  "Y": "PAPER",
  "Z": "SCISSORS",
  "A": "ROCK",
  "B": "PAPER",
  "C": "SCISSORS",
}

SCORE = {
  ("ROCK", "PAPER"): 1,
  ("PAPER", "SCISSORS"): 2,
  ("SCISSORS", "ROCK"): 3,
  ("ROCK", "ROCK"): 4, 
  ("PAPER", "PAPER"): 5,
  ("SCISSORS", "SCISSORS"): 6,
  ("ROCK", "SCISSORS"): 7,
  ("PAPER", "ROCK"): 8,
  ("SCISSORS", "PAPER"): 9,
}

BEATS = {
  "ROCK": "SCISSORS",
  "SCISSORS": "PAPER",
  "PAPER": "ROCK",
}

commands = [(SYNONYMS[a], b) for a, b in [line.split() for line in inputs.REAL.split("\n")]]

def what_should_i_play(them, command):
  return them if command == "Y" \
    else BEATS[them] if command == "X" \
    else next(iter(set(BEATS.keys()) - set([them, BEATS[them]])))

print(f"Part 1: {sum(SCORE[SYNONYMS[me], them] for them, me in commands)}")
print(f"Part 2: {sum(SCORE[what_should_i_play(them, me), them] for them, me in commands)}")


