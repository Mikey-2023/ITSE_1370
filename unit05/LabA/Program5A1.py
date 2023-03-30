with open("/unit05/LabA/LabA-Text-Files/Lab5A1.txt", 'r') as rf:
    listVar = rf.read().split()
    for i in range(len(listVar)):
        listVar[i] = int(listVar[i])

    total = 0
    for i in range(5):
        total += listVar[i]
    print("The total of the first five numbers in the list is", total)

    inputNum = int(input("Enter a number: "))
    total1 = 0
    for i in range(len(listVar)):
        if listVar[i] == inputNum:
            total1 += 1
    print("The number you entered appears", total1, "times in the list.")

    inputNum1 = int(input("Enter another number: "))
    while inputNum1 in listVar:
        listVar.remove(inputNum1)
    print("Here's the list, with that number removed:")
    print(listVar)
