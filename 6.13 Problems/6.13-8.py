# Write a function areaOfCircle(r) which returns the area of a circle of radius r.
# Make sure you use the math module in your solution.

import math


def areaOfCircle(r):
    area = (math.pi * (r**2))
    return area

circleRadius = int(input("Radius of Circle: "))

print("Area of circle is ", areaOfCircle(circleRadius))