# Write a function findHypot. The function will be given the length of two sides of a right-angled triangle and it
# should return the length of the hypotenuse. (Hint: x ** 0.5 will return the square root, or use sqrt from the math
# module)

import math

def findHypot(legA, LegB): # Function

    legApow2 = legA**2
    legBpow2 = LegB**2

    hypot = math.sqrt(legApow2+legBpow2)

    return hypot

print("Welcome to the hypotenuse finder!")
legAQuestion = int(input("What is the side of leg A: "))
legBQuestion = int(input("What is the side of leg B: "))

print(findHypot(legAQuestion,legBQuestion))