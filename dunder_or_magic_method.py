#A dunder method in Python is a special method whose name starts and ends with two underscores.

#Dunder = Double UNDERscore
#Dunder methods are special Python methods that let you define how your objects behave when Python performs built-in operations on them.

class Author:

  def __init__(self, name, book_name, pages):
    self.name = name
    self.book_name = book_name
    self.pages = pages

  def __len__(self):           #here this len is we defined 
    return self.pages

  def __str__(self):           # this is also
    return f"{self.book_name} by {self.name}"

  def __call__(self, *args, **kwargs):    # this is alsoo
    print("hi")

  def __del__(self):                       # this is also
    print("Author object has been deleted")


d = Author("Jenny", "Python Basic to Advance", 300)
print(len(d))
print(d)
d()
del d
print(d)