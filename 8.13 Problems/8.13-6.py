import turtle
import random

def isInScreen(w,t):
    leftWall = w.window_width() / -2
    rightWall = w.window_width() / 2
    topWall = w.window_height()/ 2
    bottomWall = w.window_height() / -2

    turtleX = t.xcor()
    turtleY = t.ycor()

    if turtleX < leftWall or turtleX > rightWall or turtleY > topWall or turtleY < bottomWall:
        t.left(180)
        return False

    return True

def randomWalk(w,t,t2):
    counter = 0

    while True:
        while isInScreen(w,t):
            randomRange = random.randrange(0, 120)  # Decides how wide the angle the turns are
            leftOrRight = random.randrange(0, 2)  # Decide if we turn right or left

            randomRange2 = random.randrange(0, 120)  # Decides how wide the angle the turns are
            leftOrRight2 = random.randrange(0, 2)  # Decide if we turn right or left



            if (leftOrRight == 1):
                t.left(randomRange)
                t.forward(20)
                t2.left(randomRange2)
                t2.forward(20)

                if (t.pos() == t2.pos()):
                    wn.bgcolor('red')
            else:
                t.right(randomRange)
                t.forward(20)
                t2.right(randomRange2)
                t2.forward(20)

                if (t.pos() == t2.pos()):
                    wn.bgcolor('red')



wn = turtle.Screen()
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()

turtle1.color('red')
turtle2.color('green')


randomWalk(wn,turtle1,turtle2)


wn.exitonclick()
