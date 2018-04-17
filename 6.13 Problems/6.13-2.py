#Write a program to draw this. Assume the innermost
#square is 20 units per side, and each successive
# square is 20 units bigger, per side, than the one inside it.

import turtle


def drawSquare(amountOfSquares):

    sizeOfSquare = 20
    minusSquare = 5

    for i in range(amountOfSquares):
        square.penup()
        square.left(90)
        square.forward(10)
        square.right(90)
        square.back(minusSquare)
        square.pendown()


        for i in range(4):
            square.forward(sizeOfSquare)
            square.right(90)

        square.forward(minusSquare)

        newSquare = sizeOfSquare + 20
        sizeOfSquare = newSquare
        newMinusSquare = minusSquare + 5
        minusSquare = newMinusSquare
        print("Size of Square: ", sizeOfSquare)
        print("Backwards move: ", minusSquare)





square = turtle.Turtle()
wn = turtle.Screen()


drawSquare(4)



wn.exitonclick()