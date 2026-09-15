class Rectangle:
    def __init__(self,length,width):
        self.rect_len=length
        self.rect_wid=width
    def get_area(self):
        return self.rect_len*self.rect_wid
        

rect_area=Rectangle(10,5)
rect_area_2 =Rectangle(20,20)
print(rect_area.get_area())
print(rect_area_2.get_area())   
rect_area_3=Rectangle(0,2)
print(rect_area_3.get_area())
rect_area_4=Rectangle(0,0)
print(rect_area_4.get_area())
             