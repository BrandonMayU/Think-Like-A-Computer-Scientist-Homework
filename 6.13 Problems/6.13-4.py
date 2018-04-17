#Draw this pretty pattern.
import turtle

square = turtle.Turtle()
wn = turtle.Screen()

def drawSquare(turtle, size, totalSquares):

    rotationAngle = 360/totalSquares

    for i in range(totalSquares):
        square.right(rotationAngle)

        for i in range(4):
            square.forward(size)
            square.right(90)



drawSquare(square,200,20)



wn.exitonclick()