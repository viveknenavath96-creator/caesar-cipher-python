# One parent → one child.

class Human:
    def __init__(self,eyes,nose):
        self.num_eyes=eyes
        self.num_nose=nose

    def eat(self):
        print("A human can eat")
    def work(self):
        print("can work")

class Male(Human):
    def __init__(self,name,eyes,nose):
        super().__init__(eyes,nose)
        self.name=name
    def study(self):
        super().work()
        print("studying python")    
    def work(self):
        print("can code")
    def display(self):
        print(f"I'm {self.name} , I have {self.num_nose} nose and {self.num_eyes} eyes")

num=Male("vivek",2,1)
print(num.name)
print(num.num_eyes)
print(num.num_nose) 
num.study()
num.work()
num.eat()  
num.display()             

#h=Male()
#h.work()
#h.study()