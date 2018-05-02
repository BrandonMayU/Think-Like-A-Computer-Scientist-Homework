import random
import turtle

def isInScreen(w, t):
    if random.random() > -0.20:
        return  True
    else:
        return False


t = turtle.Turtle()
wn = turtle.Screen()

t.shape('turtle')


while(isInScreen(wn,t)):
    randomRange = random.randrange(0,120) #Decides how wide the angle the turns are
    leftOrRight = random.randrange(0,2) #Decide if we turn right or left

    if(leftOrRight == 1):
        t.left(randomRange)
        t.forward(20)
    else:
        t.right(randomRange)
        t.forward(20)



wn.exitonclick()