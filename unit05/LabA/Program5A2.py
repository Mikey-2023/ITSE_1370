# Program5A2
# Michael Camp
# This program takes a list of fifteen random integers, and prints a list of the odds, a list of the evens,
# and how many of each are in the original list of fifteen

import random

listVar = []
for i in range(15):
    listVar.append(random.randint(1, 20))
print(listVar)

totalOdd = 0
totalEven = 0
listOdd = []
listEven = []
for i in range(len(listVar)):
    if listVar[i] % 2 == 1:
        totalOdd += 1
        listOdd.append(listVar[i])
    else:
        totalEven += 1
        listEven.append(listVar[i])
print("There were", totalOdd, "odd numbers in the list.")
print(listOdd)
print("There were", totalEven, "even numbers in the list.")
print(listEven)
