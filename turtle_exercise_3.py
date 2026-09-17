from turtle import Turtle,Screen
s1=Screen()
tom=Turtle()

def move_forward():
    tom.forward(10)
def move_backward():
    tom.backward(10)
def turn_left():
    tom.left(20)
    #new_heading=tom.heading()+20
    #om.setheading(new_heading)
    tom.forward(10)
def turn_right():
    tom.right(20)
    #new_heading=tom.heading()-20
    #tom.setheading(new_heading)
    tom.forward(10)
def clear_screen():
    tom.clear() 
    tom.penup()
    tom.home()
    tom.pendown()
s1.listen()
s1.onkey(fun=move_forward,key="f")
s1.onkey(fun=move_backward,key="b")
s1.onkey(fun=turn_left,key="l")
s1.onkey(fun=turn_right,key="r")
s1.onkey(fun=clear_screen,key="c")

s1.exitonclick()