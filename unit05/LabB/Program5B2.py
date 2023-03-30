# Program5B2
# Michael Camp
# This program gets valid variable names by ensuring what the user enters does not contain illegal characters or words
def main():
    def valid_char(char):
        # True if char is valid for variable name
        return char.isnumeric() or char.isalpha() or char == "_"

    with open("Lab5B2.txt", 'r') as rf:
        reserved_words = tuple(word.strip() for word in rf.read().split())
        print("These words are reserved:", reserved_words)

        input_name = input("Please enter a variable: ")
        valid_name = True

        if input_name in reserved_words:
            print("This word is reserved")
            valid_name = False

        if input_name[0].isnumeric():
            print("The first character cannot be a number.")
            valid_name = False

        for letter in input_name:
            if not valid_char(letter):
                print("Variable names can only contain letters, numbers, and underscores:", end=' ')
                print(letter, "is invalid")
                valid_name = False  # TODO: This really should only execute once

        if valid_name:
            print("That name works!")


if __name__ == '__main__':
    main()
