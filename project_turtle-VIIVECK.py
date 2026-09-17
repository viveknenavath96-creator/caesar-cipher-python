import random
from turtle import Turtle,Screen

def no_of_turtles():
    count=0
    while True:
        count=int(input("Enter the number of turtle upto range(2-10)"))
        if 2<=count<=10:
          return count
        else:
             print("out of range , please enter in range")

turtles=no_of_turtles()   
print(turtles)

s1=Screen()
s1.exitonclick()