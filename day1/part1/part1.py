import re

def main():
    # load input.txt into a list of strings
    with open("input.txt", "r") as f:
        data = f.read().splitlines()

    # for each string in the list, which are numbers and letters, find
    # the first number using regex
    add = 0
    for i in range(len(data)):
        matches = re.findall(r"\d", data[i])
        code = int("{}{}".format(matches[0], matches[-1]))
        add += code

    print(add)

if __name__ == "__main__":
    main()
