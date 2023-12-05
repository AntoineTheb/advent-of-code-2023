from functools import reduce
from operator import mul

def process(line):
    # For the string in 'line', remove everything before ':'. Then,
    # split on ';'. Then, split on ','. Then, split on ' '. Then,
    # add the key-value pairs to a dictionary. Return the dictionary.

    # Example: Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    game = line.split(": ")[1]
    sets = []
    mins = dict({'red': 0, 'green': 0, 'blue': 0})
    for s in game.split("; "):
        boxes = s.split(", ")
        for box in boxes:
            amount, color = box.split(None, 2)
            mins[color] = max(mins[color], int(amount))

    return mins

def main():

    # Load test.txt into a list of strings
    with open("input.txt", "r") as f:
        lines = f.readlines()
    tally = 0
    for i, line in enumerate(lines):
        mins = process(line)
        values = mins.values()
        power = reduce(mul, values)
        tally += power

    print("Tally: {}".format(tally))


if __name__ == "__main__":
    main()
