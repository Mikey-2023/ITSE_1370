# Lab6A1
# Michael Camp
# This program calculates areas of squares/hexagons/octagons based on side/length values from a file
import math


def square(s):
    area = s ** 2
    print("Area of the square:", round(area, 2))


def hexagon(s):
    area = (3 * math.sqrt(3) * s ** 2) / 2
    print("Area of the hexagon:", round(area, 2))


def octagon(s):
    area = 2 * s ** 2 * (1 + math.sqrt(2))
    print("Area of the octagon:", round(area, 2))


def main():
    with open("Lab6A1.txt", 'r') as rf:
        for line in rf.readlines():
            line = line.split()
            sides, length = int(line[0]), float(line[1])
            if sides == 4:
                square(length)
            elif sides == 6:
                hexagon(length)
            elif sides == 8:
                octagon(length)


if __name__ == '__main__':
    main()
