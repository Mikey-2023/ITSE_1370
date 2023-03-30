# Program4B3
# Michael Camp
# This program reads a file with names and outputs them in an alternate format

with open("Lab4B3.txt", "r") as fr:
    namesFile = fr.read()
    namesList = namesFile.split("\n")

    for element in namesList:
        lastName = element.split(", ")[0]
        firstName = element.split(", ")[1]
        initialVar = element.split(", ")[2]
        print(firstName, initialVar, lastName)
