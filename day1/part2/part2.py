import regex as re

formatter = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six" : 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

def main():
    # load input.txt into a list of strings
    with open("test.txt", "r") as f:
        data = f.read().splitlines()

    # for each string in the list, which are numbers and letters, find
    # the first number using regex
    add = 0
    for i in range(len(data)):
        r = re.compile("\\d|one|two|three|four|five|six|seven|eight|nine")
        matches = re.findall(r, data[i], overlapped=True)
        print(matches)
        code = int("{}{}".format(formatter[matches[0]], formatter[matches[-1]]))
        add += code

    print(add)


if __name__ == "__main__":
    main()
