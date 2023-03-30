# Program4B2
# Michael Camp
# This program reads a file with two strings and outputs them in a different order

with open("Lab4B2.txt", "r") as fr:
    SV = fr.read()
SSV = SV.split()
SSV1 = SSV[0]
SSV2 = SSV[1]
LS = len(SSV1)  # Could have used SSV2 just the same -- since their lengths are the same it doesn't matter
finalString = ""
for i in range(LS):
    finalString += (SSV1[i]+SSV2[i])
print("This is the final string:", finalString)
