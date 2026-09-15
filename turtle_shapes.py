import random
from turtle import Turtle,Screen
s1=Screen()
tom = Turtle()
colors=["pink","red","violet","green","blue4","BlueViolet","DarkOrange4","DimGray"]
for i in range(3,9):
    angle=360/i
    tom.pencolor(random.choice(colors))
    for _ in range(i):
        tom.forward(100)
        tom.right(angle)
s1.exitonclick
#tom.screen.mainloop()        