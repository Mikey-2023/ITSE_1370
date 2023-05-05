# Lab9A1
# Michael Camp
# This program creates a class 'DistanceCalculator' whose objects find and store the distance between two
# points on the Cartesian plane through a method 'distanceComputation' into an instance variable 'distance'
import math


class DistanceCalculator:
    def __init__(self, x1: float, y1: float, x2: float, y2: float):
        """Creates objects given two points on the Cartesian plane"""
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def distanceComputation(self):
        """Calculates the distance between the given two points"""
        self.distance = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)

    def __str__(self):
        return "x1: {}, x2: {}, y1: {}, y2: {}, distance: {}".format(round(self.x1, 2), round(self.x2, 2),
                                                                     round(self.y1, 2), round(self.y2, 2),
                                                                     round(self.distance, 2))


def main():
    distance_calculation1 = DistanceCalculator(1, 1, 2, 1)
    distance_calculation1.distanceComputation()
    print(distance_calculation1)

    distance_calculation2 = DistanceCalculator(1, 1, -2, 2)
    distance_calculation2.distanceComputation()
    print(distance_calculation2)


if __name__ == '__main__':
    main()
