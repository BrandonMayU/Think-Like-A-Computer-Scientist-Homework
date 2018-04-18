import turtle


#This function gets called to draw the square
def drawSquare():
    square.penup()
    square.goto(radius / 2, -radius / 2)
    square.pendown()
    square.circle(radius * hypotenuse, steps=4)



hypotenuse = (2 ** 0.5) / 2

screen = turtle.Screen() #Start Screen

squareSize = 20 #Preset the sqaure size for easy changes

square = turtle.Turtle() #Reference the actual turtle to call

square.setheading(45) #Set the heading so you don't get diamonds

#Use a for loop to repeadtly create squares
for radius in range(squareSize, squareSize * 5 + 1, squareSize):
    drawSquare()

screen.exitonclick()