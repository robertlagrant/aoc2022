import inputs

ALIAS = {
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

def what_should_i_play(them, command):
  match command:
    case "X": return BEATS[them]                                    # lose
    case "Y": return them                                           # draw
    case "Z": return next(k for k, v in BEATS.items() if v == them) # win

commands = [(ALIAS[a], b) for a, b in [l.split() for l in inputs.REAL.split("\n")]]

print(f"Part 1: {sum(SCORE[ALIAS[me], them] for them, me in commands)}")
print(f"Part 2: {sum(SCORE[what_should_i_play(them, c), them] for them, c in commands)}")

