# ONE PARENT FROM , FROM PARENT CLASS MULTIPLE CHILDREN 
# One parent → multiple children
class Parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("calling init from parent")
        
    def eat(self):
        print("i can eat")

    def work(self):
        print("i can do work")

class Son(Parent):
    def __init__(self, name, age,location):
        Parent.__init__(self,name,age)
        self.location=location
        print("calling init from Son")

    def sleep(self):
        print("i can sleep more")

    def games(self):
        print("i can play games")

class Daughter(Parent):
    def __init__(self, name, age,can_dance):
        Parent.__init__(self,name, age)
        self.can_dance=can_dance
        print("calling init from daughter")
    
    def cook(self):
        print("i can cook")

    def work(self):
        Parent.work(self)
        Parent.eat(self)
        print("i can do home works")    

parent_1=Parent("Ghansiram",40)
print(parent_1.name)
print(parent_1.age)

son_1=Son("Vivek",20,"Hyderabad")
print(son_1.name)
print(son_1.age)
print(son_1.location)

female_1=Daughter("suma",19,True)
print(female_1.name)
print(female_1.age)
print(female_1.can_dance)

# female_1=Daughter()
# female_1.work()

# male_1=Son()
# male_1.work()   
