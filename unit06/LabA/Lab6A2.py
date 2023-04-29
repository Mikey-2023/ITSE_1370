# Lab6A2
# Michael Camp
# This program adds the digits of numbers from a file

def addDigits(str_num):
    """Takes a string of a number and creates a list where each element is a converted
       digit from the string, and returns the sum of said digits"""
    list_nums = [int(x) for x in str_num]
    return sum(list_nums)


def main():
    with open("Lab6A2.txt", 'r') as rf:
        for line in rf:
            print(line.strip(), addDigits(line.strip()))


if __name__ == '__main__':
    main()
