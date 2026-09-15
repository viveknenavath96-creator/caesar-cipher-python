# ONE PARENT CLASS , 1,2,3,........N CHILD CLASS FROM PARENT CLASS
# Grandparent → Parent → Child.

class Human:
    def __init__(self,heart):
        self.eyes=2
        self.heart=heart

    def eat(self):
        print("I'm eating lunch")

    def work(self) :
        print("i can do work")

class Male(Human):
    def __init__(self,name):
        self.name=name

    def sleep(self):
         print("i'm sleeping")

    def work(self):
        Human.work(self)
        print("i can do code") 

class Boy(Male):
    def __init__(self, name,heart,games):
        Human.__init__(self,heart)
        Male.__init__(self,name)
        self.games=games

    def play(self):
        print("i can play games")

    def work(self):
        Male.work(self)
        #Human.work(self)
            
boy_1=Boy("vivek",1,"volleyball")
print(boy_1.name)
print(boy_1.heart)
print(boy_1.games)
print(boy_1.eyes)
boy_1.work()
                
