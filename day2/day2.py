#  A = Rock, B = Paper, C = Scissors
#  X = Rock, Y = Paper, Z = Scissors
#  X = 1, Y = 2, Z = 3
# Win = +6, Lose = 0, Draw = +3

combinations = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6
}

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f]

total = 0

for line in lines:
    total += combinations[line]

print(total)

# X = Lose, Y = Draw, Z = Win

combinations_2 = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7
}

total = 0

for line in lines:
    total += combinations_2[line]

print(total)
