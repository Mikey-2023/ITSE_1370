# Program5A3
# Michael Camp
# Determines if a list of ints is going up, down, or neither

with open("/Users/michaelcamp/PycharmProjects/ITSE-1370/unit05/LabA/LabA-Text-Files/Lab5A34.txt", 'r') as rf:
    listNums = rf.read().split()
    for i in range(len(listNums)):
        listNums[i] = int(listNums[i])
    print(listNums)

    increasing = True
    for j in range(len(listNums) - 1):
        if not (listNums[j] < listNums[j + 1]):
            increasing = False
            break

    decreasing = True
    for k in range(len(listNums) - 1):
        if not (listNums[k] > listNums[k + 1]):
            decreasing = False
            break

    if increasing:
        print("Going up!")
    elif decreasing:
        print("Going down!")
    else:
        print("Not going up, not going down")
