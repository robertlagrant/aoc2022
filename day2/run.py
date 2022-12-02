import inputs

BEATS = {
  "ROCK": "SCISSORS",
  "SCISSORS": "PAPER",
  "PAPER": "ROCK",
}


def score(me, them):
  match me:
    case "ROCK": score = 1
    case "PAPER": score = 2
    case "SCISSORS": score = 3

  return score + (3 if me == them else 6 if BEATS[me] == them else 0)


def alias(command):
  match command:
    case "X" | "A": return "ROCK"
    case "Y" | "B": return "PAPER"
    case "Z" | "C": return "SCISSORS"


def what_should_i_play(them, command):
  match command:
    case "X": return BEATS[them]                                    # lose
    case "Y": return them                                           # draw
    case "Z": return next(k for k, v in BEATS.items() if v == them) # win


commands = [(alias(a), b) for a, b in [l.split() for l in inputs.REAL.split("\n")]]

print(f"Part 1: {sum(score(alias(me), them) for them, me in commands)}")
print(f"Part 2: {sum(score(what_should_i_play(them, c), them) for them, c in commands)}")

