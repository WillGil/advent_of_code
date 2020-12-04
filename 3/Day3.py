def main(input):
    print(p1(input))
    print(p2(input))


def p1(input):

    index = 0
    count = 0

    for line in input:
        linelen = len(line)

        if index >= linelen:
            index -= linelen

        if line[index] == "#":
            count += 1

        index += 3
    return count


def p2(input):
    return (
        find_slope_trees(input, 1, 1)
        * find_slope_trees(input, 1, 3)
        * find_slope_trees(input, 1, 5)
        * find_slope_trees(input, 1, 7)
        * find_slope_trees(input, 2, 1)
    )


def find_slope_trees(input, row, col):
    index = 0
    count = 0

    for row in range(0, len(input), row):
        print(index)
        if index >= len(input[row]):
            index -= len(input[row])

        if input[row][index] == "#":
            count += 1

        index += col

    return count


# Check module is the main program
if __name__ == "__main__":
    with open("Day3.txt", mode="r") as file:
        inp = [line.strip() for line in file]

    # Call the main method
    main(inp)