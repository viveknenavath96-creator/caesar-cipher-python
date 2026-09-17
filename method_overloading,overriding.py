class Demo:
    def add(self, a, b, c=0):        # this is default method of overloading
        return a + b + c             # without using default c = 0 it will give you error

d = Demo()
print(d.add(2, 3))
print(d.add(2, 3, 4))

#*Using args for Variable Length Arguments:

class Demo:
   def add(self, *args):      
      total = 0
      for i in args:
         total = total + i
         return total

d = Demo()
print(d.add(1, 2))
print(d.add(1, 2, 3))
print(d.add(1, 2, 3, 4, 5, 6))

# 2. Method Overriding (Inheritance)
# Method overriding allows a child class to provide a specific implementation of a method already defined in its parent class (10:48):

class Father:
   def sleep(self):
      print("sleeps from 10 p.m. to 5:00 a.m.")

class Son(Father):                               
    def sleep(self):
      print("sleeps from 2:00 a.m. to 10:00 a.m.")  

ram = Son()
ram.sleep()  # Calls Son's version


