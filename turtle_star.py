from turtle import Turtle,Screen
s1=Screen()
tom=Turtle()
tom.color("red","yellow")
tom.begin_fill()
while True:
    tom.forward(300)
    tom.left(170)
    if tom.heading()==0:
        break
tom.end_fill()
s1.exitonclick()