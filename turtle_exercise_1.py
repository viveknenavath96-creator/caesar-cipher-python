from turtle import Turtle,Screen
s1=Screen()
tom = Turtle()
for _ in range(10):
    tom.forward(10)
    tom.penup()
    tom.forward(10)
    tom.pendown()
s1.exitonclick()      