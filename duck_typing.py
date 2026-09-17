##Python doesn't care what an object is — it only cares what an object can do.

#That means Python doesn't check "is this a Dog class or a Duck class?
# " It just checks "does this object have the method I'm trying to call?
# " If yes, it runs. If no, it crashes.

class Duck:
    def sound(self):
        print("Quack Quack")

    def colour(self):
        print("Duck is in white colour") 

class Dog:
    def sound(self):
        print("Bhoww Bhoww")
    
    def colour(self):
        print("Dog is in black colour")    

class Cat:
    def sound(self):
        print("meowww meowww")
    def colour(self):
        print("cat is in white , black, brown colours")

def duckdog(object):
    object.sound()
    object.colour()       

duck=Duck()
duckdog(duck)
dog=Dog()
duckdog(dog)
cat=Cat()
duckdog(cat)
