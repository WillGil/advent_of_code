# Read the file
with open("Day4.txt", mode="r") as file:
    inp = [line.strip() for line in file]


# Required fields
checker = {
    "byr": False,
    "iyr": False,
    "eyr": False,
    "hgt": False,
    "hcl": False,
    "ecl": False,
    "pid": False,
}


validPassports = 0
# Get all relevant lines into one string
relevantEntry = ""
listOfEntries = []

for line in inp:
    print(line)
    if line:
        relevantEntry = relevantEntry + " " + line
    elif not line:
        listOfEntries.append(relevantEntry)
        relevantEntry = ""
# End of file reached
else:
    listOfEntries.append(relevantEntry)


# Find valid entries
for record in listOfEntries:
    for key in checker.keys():
        if key in record:
            checker[key] = True

    if all(value == True for value in checker.values()):
        validPassports += 1

    checker = dict.fromkeys(checker, False)


print(validPassports)
