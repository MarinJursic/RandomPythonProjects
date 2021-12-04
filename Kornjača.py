import time
import random
import turtle


Number = random.randrange(100,1000,1)

Move = 0

window = turtle.screensize(750,750,"white")

turtle.speed(5)

turtle.pensize(5)

turtle.pendown()

for x in range(Number):

    Move = random.randrange(1,4,1)

    Distance = random.randrange(10, 100, 1)

    if Move == 1:

        turtle.forward(Distance)

    if Move == 2:
        turtle.back(Distance)

    if Move == 3:
        turtle.left(Distance)

    if Move == 4:
        turtle.right(Distance)

    print(turtle.pos()[0])
    print(turtle.pos()[1])

    if turtle.pos()[0] > 400 or turtle.pos()[0] < -400 or turtle.pos()[1] > 400 or turtle.pos()[1] < -400:

        print("Bruh")

        turtle.penup()
        turtle.goto(0,0)
        turtle.settiltangle(random.randrange(0,360,90))
        turtle.pendown()


print("Turtle Complete")

time.sleep(10)