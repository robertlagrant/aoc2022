import inputs

SYNONYMS = {
  "X": "ROCK",
  "Y": "PAPER",
  "Z": "SCISSORS",
  "A": "ROCK",
  "B": "PAPER",
  "C": "SCISSORS",
}

BEATS = {
  "ROCK": "SCISSORS",
  "SCISSORS": "PAPER",
  "PAPER": "ROCK",
}

LOSES_TO = {v: k for k, v in BEATS.items()}

SCORES = {
  "ROCK": 1,
  "PAPER": 2,
  "SCISSORS": 3,
}

strategy_1_score, strategy_2_score = 0, 0

def score(them, me):
  print(them, me)
  # Score based on what we chose
  _score = SCORES[me]

  # Score based on who won
  if them == me:
    _score += 3
  elif BEATS[me] == them:
    _score += 6

  return _score

for turn in inputs.REAL.split("\n"):
  them_raw, me_raw = turn.split()
  them = SYNONYMS[them_raw]
  strategy_1_score += score(them, SYNONYMS[me_raw])

  strategy_2_score += score(them, 
    them if me_raw == "Y" 
    else BEATS[them] if me_raw == "X" 
    else LOSES_TO[them])

print(f"Part 1: {strategy_1_score}")
print(f"Part 2: {strategy_2_score}")

