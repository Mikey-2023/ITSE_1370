with open("Lab4B1.txt", 'r') as fr:
    nums = fr.read()
    numsSplit = nums.split()

for i in range(len(numsSplit)):
    numsSplit[i] = int(numsSplit[i])

sumOdds = 0
for x in numsSplit:
    if x % 2 != 0:
        print(x, end=' ')
        sumOdds += x
print()
print("The total of the odd numbers in this is", sumOdds)
