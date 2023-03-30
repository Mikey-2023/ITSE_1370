# Program5B1
# Michael Camp
# This program creates a dictionary with key-value pairs of name-age by reading a text file,
# and uses said dictionary to produce results based on user input

def main():
    dict_var = {}
    with open("Lab5B1.txt", 'r') as rf:
        for line in rf:
            line = line.split()
            name, age = line[0], int(line[1])
            dict_var[name] = age
        print("This is the dictionary:", dict_var)

        input_name = input("Enter a name: ")
        if input_name in dict_var:
            print("This is a name in the dictionary!")
        else:
            print("This is not a name in the dictionary.")

        input_age = int(input("Enter an age: "))
        age_count = list(dict_var.values()).count(input_age)
        print("The age you entered appears", age_count, "time(s) in the dictionary.")

        highest_age = 0
        for age in dict_var.values():
            if age > highest_age:
                highest_age = age
        print("The highest age in the list is", highest_age)


if __name__ == '__main__':
    main()
