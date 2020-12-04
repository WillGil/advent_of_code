def main(input):

    validPasswords = p1(input)
    print(validPasswords)

    validPasswords2 = p2(input)
    print(validPasswords2)


def p1(input):
    count = 0
    # loop through lines
    for line in input:
        lineSplit = line.split()

        # Count occurances
        occurances = lineSplit[2].count(lineSplit[1][0])

        # Split first string based on -
        range = lineSplit[0].split("-")

        if int(range[0]) <= occurances <= int(range[1]):
            count = count + 1

    return count


def p2(input):
    count = 0
    for line in input:
        lineSplit = line.split()

        # Get Indexes
        indexes = lineSplit[0].split("-")

        # Char that is being looked for
        charSearchingFor = lineSplit[1][0]

        print(
            f"Looking for {charSearchingFor} Index postion contains:"
            + lineSplit[2][int(indexes[0]) - 1]
        )
        if (
            lineSplit[2][int(indexes[0]) - 1] == charSearchingFor
            and not lineSplit[2][int(indexes[1]) - 1] == charSearchingFor
        ):
            count = count + 1
            continue
        elif (
            lineSplit[2][int(indexes[1]) - 1] == charSearchingFor
            and not lineSplit[2][int(indexes[0]) - 1] == charSearchingFor
        ):
            count = count + 1
            continue

    return count


# Check module is the main program
if __name__ == "__main__":
    fileinput = ""
    with open("Day2.txt", mode="r") as file:
        fileinput = file.readlines()

    # Call the main method
    main(fileinput)