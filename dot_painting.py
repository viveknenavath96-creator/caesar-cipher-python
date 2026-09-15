import random
import turtle
from turtle import Turtle,Screen
tom=Turtle()
s1=Screen()
turtle.colormode(255)
tom.penup()
tom.speed("fast")
for _ in range(300):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    tom.pencolor((r,g,b))
    tom.dot(20)
    tom.goto(random.randint(-300,300),random.randint(-300,300))

s1.exitonclick