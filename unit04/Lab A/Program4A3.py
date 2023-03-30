# Program4A3
# Michael Camp
# This program takes a password until one is given that meets three requirements

SET_NUMS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SET_CHARS = ["!", "&", "*", "%", "$"]
passwordVar = input("Enter your password: ")

for num in SET_NUMS:
    if num in passwordVar:
        hasNum = True
        break
    else:
        hasNum = False

for char in SET_CHARS:
    if char in passwordVar:
        hasChar = True
        break
    else:
        hasChar = False

while (len(passwordVar) < 8) or (not hasNum) or (not hasChar):
    if len(passwordVar) < 8:
        print("Your password should be at least 8 characters.")
    if not hasNum:
        print("Your password should contain a number.")
    if not hasChar:
        print("Your password should contain a special character from the list !, &, *, %, $.")

    passwordVar = input("Enter your password: ")

    for num in SET_NUMS:
        if num in passwordVar:
            hasNum = True
            break
        else:
            hasNum = False

    for char in SET_CHARS:
        if char in passwordVar:
            hasChar = True
            break
        else:
            hasChar = False

print("You set your password to be:", passwordVar)
