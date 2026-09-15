class Student:
    def __init__(self,name,ph_num,age):
        self.name=name    # name is public variable
        self._ph_num=ph_num  # _ph_num is protected variable (indicates with one underscore)  
        self.__age=age     ## age is private variable(indicates double underscores AND within the class we can access)
    def __display(self):
        print(f"Hyyy my name is {self.name} , my mobile number is {self._ph_num} , from Student class")
        print(f"My age is {self.__age}")
    def displayprivatedata(self):
        self.__display()   

class Branch(Student):
    def show(self):
        print(f"MY age is {self.__age} from branch class")        

s1=Student("vivek",123456789,20)
#print(s1.name)
#print(s1._ph_num)
#print(s1._Student__age)
#s1._Student__display()      ## WE CAN ALSO USE THE PRIVATE VARIABLE , BY USING NAME MANGLING (dir()) TO ACCESS _BASECLASS_NAME__METHOD :
#s1.age()   
#b1=Branch("NAME",000000,25)
#print(dir(b1))
#print(b1._Branch__age)
#1.show()
s1.displayprivatedata()
