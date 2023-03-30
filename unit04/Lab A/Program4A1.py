# Program4A1
# Michael Camp
# This program takes two words from the user and outputs some info about how they relate to each other

word1 = input("Enter a word: ")
word2 = input("Enter another word: ")

if (word1[0] == word2[0]) and (word1[len(word1)-1] == word2[len(word2)-1]):
    print("The words you've entered have the same first and last letters. Cool!")
else:
    print("The words you've entered don't have the same first and last letters.")

if word2 in word1:
    print("The second word you entered is contained within the first. Very cool!")
else:
    print("The second word you've entered is not contained within the first.")
