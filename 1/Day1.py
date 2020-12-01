# Run code and print result
def main(input):
    data = [int(line) for line in input]
    print(p1(data, 2020))
    print(p2(data, 2020))


def p1(d, target):
    for val in d:
        if target - val in d:
            return val * (target - val)


def p2(d, target):
    for i in d:
        for j in d:
            if target - i - j in d:
                return i * j * (target - i - j)


# Check module is the main program
if __name__ == "__main__":
    fileinput = ""
    with open("Day1.txt", mode="r") as file:
        fileinput = file.readlines()

    # Call the main method
    main(fileinput)
