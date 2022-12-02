from enum import Enum

import inputs


class Guess(Enum):
  rock = 1
  paper = 2
  scissors = 3

  @property
  def beats(self):
    return list(Guess)[(self.value - 2) % len(Guess)]
  
  @property
  def beaten_by(self):
    return list(Guess)[(self.value) % len(Guess)]


def alias(command):
  match command:
    case "X" | "A": return Guess.rock
    case "Y" | "B": return Guess.paper
    case "Z" | "C": return Guess.scissors


def what_should_i_play(them, command):
  match command:
    case "X": return them.beats      # lose
    case "Y": return them            # draw
    case "Z": return them.beaten_by  # win


def score(me, them):
  return me.value + (6 if me.beats == them else 3 if me == them else 0)


commands = [(alias(a), b) for a, b in [l.split() for l in inputs.REAL.split("\n")]]

print(f"Part 1: {sum(score(alias(me), them) for them, me in commands)}")
print(f"Part 2: {sum(score(what_should_i_play(them, c), them) for them, c in commands)}")

