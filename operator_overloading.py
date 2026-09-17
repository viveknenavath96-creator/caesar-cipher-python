#Operator overloading lets you define how operators like +, -, ==, <, etc.
# behave for objects of your own classes. Python does this through special "dunder" (double underscore) methods.

# Operator	Method    
# +	       __add__
# -	       __sub__
# *	       __mul__
# /	       __truediv__
# ==	    __eq__
# <	       __lt__
# >	       __gt__
# len()	   __len__
# str()	   __str__
# []	     __getitem__

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __gt__(self, other):
        if self.age > other.age:
           return True
        else:
            return False           
        

p1=Person("vivel",20)
p2=Person("vivek",21)
if p1>p2:
    print(f" {p1.name} will pay the bill")      
else:
    print(f" {p2.name} will pay the bill")


class Complexnumber:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i
    def __add__(self, other):
        return f"{self.real + other.real} + {self.imaginary + other.imaginary} i"

c1=Complexnumber(1,2)
c2=Complexnumber(4,5)
print(c1+c2)                