# Program4B1
# Michael Camp
# This program reads a file with numbers and outputs the sum of the odd ones

with open("Lab4B1.txt", 'r') as fr:
    nums = fr.read()
    numsSplit = nums.split()

numsSplitConvert = numsSplit 

for x in range(len(numsSplit)):
    numsSplitConvert[x] = int(numsSplit[x])

sumVar = 0
for y in numsSplitConvert:
    if y % 2 == 1:
        print(y, end=" ")
        sumVar += y
print()
print("The sum of the odd numbers is", sumVar)
