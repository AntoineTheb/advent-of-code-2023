
def process(line):
    # For the string in 'line', remove everything before ':'. Then,
    # split on ';'. Then, split on ','. Then, split on ' '. Then,
    # add the key-value pairs to a dictionary. Return the dictionary.

    # Example: Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    game = line.split(": ")[1]
    sets = []
    maxes = dict({'red': 0, 'green': 0, 'blue': 0})
    for s in game.split("; "):
        boxes = s.split(", ")
        for box in boxes:
            amount, color = box.split(None, 2)
            maxes[color] = max(maxes[color], int(amount))

    return maxes

def main():

    # Load test.txt into a list of strings
    with open("input.txt", "r") as f:
        lines = f.readlines()
    hardmaxes = dict({'red': 12, 'green': 13, 'blue': 14})
    tally = 0
    for i, line in enumerate(lines):
        maxes = process(line)
        bad = False
        for k, v in maxes.items():
            if v > hardmaxes[k]:
                bad = True
        if bad is False:
            tally = tally + (i + 1)

    print("Tally: {}".format(tally))


if __name__ == "__main__":
    main()
