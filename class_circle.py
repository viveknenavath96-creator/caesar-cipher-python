class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
        self.area=2*self.pi*self.radius

circle_area=Circle(5)
print(round(circle_area.area))
circle_area_2=Circle(10)
print(round(circle_area_2.area))

class Add:
    def __init__(self,a,b):
        self.first_num=a
        self.second_num=b
        self.total=self.first_num+self.second_num
numbers=Add(5,5)
numbers_1=Add(1,99)
print(numbers.total)  
print(numbers_1.total)        
