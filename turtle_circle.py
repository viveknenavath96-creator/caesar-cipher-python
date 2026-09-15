from turtle import Turtle,Screen
import random
import turtle
tom=Turtle()
s1= Screen()
tom.speed("fast")
turtle.colormode(255)
#om.begin_fill()
while True:
   r=random.randint(0,255)
   g=random.randint(0,255)
   b=random.randint(0,255)
   tom.pencolor((r,g,b))
   tom.circle(100)
   tom.left(5)
   if tom.heading()==0:
      break
#tom.end_fill()
s1.exitonclick()
   