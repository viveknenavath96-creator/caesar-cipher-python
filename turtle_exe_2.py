from turtle import Turtle
import turtle
import random
#tom=Turtle()
yes=Turtle()
yes.pensize(10)
yes.shape("turtle")
print(yes.shape())
#tom.pensize(10)
#tom.shape("turtle")
#tom.speed("fast")
turtle.colormode(255)
for _ in range(50):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    yes.pencolor((r,g,b))
    yes.seth(random.randrange(0,360,90))
    yes.forward(50)

    #tom.pencolor((r,g,b))
    #tom.setheading(random.randrange(0,360,90))
    #tom.forward(30)

turtle.exitonclick()  
    