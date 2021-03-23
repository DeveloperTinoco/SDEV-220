

import math


class Triangle():

    # Initializes variables and their values
    def __init__(self, side1=2.0, side2=2.0, side3=2.0, color=' ', filled=' '):
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
        self.__color = color
        self.__filled = filled

    # Returns side 1
    def get_side1(self):
        return self.__side1

    # Returns side 2
    def get_side2(self):
        return self.__side2

    # Returns side 3
    def get_side3(self):
        return self.__side3

    # Calulates and returns the area of the triangle
    def get_area(self):
        S = ((self.__side1 + self.__side2 + self.__side3)) / 2
        A = (S * ((S - self.__side1) * (S - self.__side2) * (S - self.__side3)))
        area = math.sqrt(A)
        return area

    # Calculates and returns the peremeter of the triangle
    def get_perimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    # Returns the color of the triangle
    def get_color(self):
        return self.__color

    # Checks to see if the triangle is filled or empty and returns the value
    def is_filled(self):
        if self.__filled == 0:
            self.__filled = False
        else:
            self.__filled = True
        return self.__filled


# Runs the program with the designated user input
if __name__ == "__main__":
    side1 = float(input("Enter the first side of the triangle: "))
    side2 = float(input("Enter the second side of the triangle: "))
    side3 = float(input("Enter the third side of the triangle: "))
    color = input("Enter the color of the triangle: ")
    filled = int(input("Enter 1 (Fill) or 0 (Not filled): "))

    # Creates an instance of the Triangle class
    myTriangle = Triangle(side1, side2, side3, color, filled)

    print("The area of the triangle is " + str(myTriangle.get_area()) + ".\n"
          "The perimeter of the triangle is " +
          str(myTriangle.get_perimeter()) + ".\n"
          "The color of the triangle is " + str(myTriangle.get_color()) + ".\n"
          "The triangle is filled: " + str(myTriangle.is_filled()) + ".\n")
