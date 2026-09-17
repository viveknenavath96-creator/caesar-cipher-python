import random
from turtle import Turtle,Screen
WIDTH,HEIGHT=600,600
color_list = ["red", "green", "pink", "yellow", "black", "brown", "blue", "orange", "aquamarine", "purple"]
def no_of_turtles():
    count=0
    while True:
        count=input("Enter the number of turtle upto range(2-10)")
        if count.isdigit():
            count=int(count)
        else:
            print("Sorry , You have entered wrong input. please re-enter the numeric input....")    
            continue
        if 2<=count<=10:
          return count
        else:
             print("out of range , please enter in range")

turtles=no_of_turtles()   
print(turtles)
s1=Screen()
s1.setup(600,600)
x_spacing=WIDTH//(turtles+1)
turtle_list=[]
for i in range(1,turtles+1):
    new_turtles=Turtle()
    new_turtles.shape("turtle")
    new_turtles.left(90)
    new_turtles.color(color_list[i-1])
    new_turtles.penup()
    new_turtles.goto(-WIDTH //2+ (i * x_spacing) ,-HEIGHT//2+10)
    turtle_list.append(new_turtles)

def race():
    is_race_on=True
    while is_race_on:
       for t in turtle_list:
          distance=random.randrange(1,20)
          t.forward(distance)
          x,y=t.pos()
          if y>=HEIGHT//2-20:
              print(f"The winner is {t.pencolor()} Turtle")
              is_race_on=False

race()

s1.exitonclick()    



