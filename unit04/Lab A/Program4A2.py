# Program4A2
# Michael Camp
# This program takes a sentence and outputs the first letter of each word as a string without spaces

sentenceVar = input("Enter a sentence: ")
sentenceVarSplit = sentenceVar.split()

for x in sentenceVarSplit:
    print(x[0], end='')
