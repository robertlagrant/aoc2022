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

LOSES_TO = {v: k for k, v in BEATS.items()}

strategy_1_score, strategy_2_score = 0, 0

for turn in inputs.REAL.split("\n"):
  them_raw, me_raw = turn.split()
  them = SYNONYMS[them_raw]

  strategy_1_score += SCORE[(SYNONYMS[me_raw], them)]
  strategy_2_score += SCORE[( 
    them if me_raw == "Y" 
    else LOSES_TO[them] if me_raw == "X" 
    else BEATS[them], them)]

print(f"Part 1: {strategy_1_score}")
print(f"Part 2: {strategy_2_score}")

