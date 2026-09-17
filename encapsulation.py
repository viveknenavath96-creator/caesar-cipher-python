## IN ENCAPSULATION PRIVATE ATTRIBUTE WE CAN READ IT AND MODIFY IT BUY USING THE getter , setter method 
# getter is used to read the private value   
# setter is used to modify the private value   {Use these method s as a good programmer }

class Student:  

    def __init__(self,name,ph_num,age):
        self.name=name    
        self._ph_num=ph_num   
        self.__age=age   

    def get_age(self):
        print( f"My age is {self.__age}")      

    def set_age(self,age):
        if age>35:
            print("you are eligible") 
        else:
            self.__age=age

    def display(self):
        print(f"Hyyy my name is {self.name} , my mobile number is {self._ph_num} , My age is {self.__age} from Student class")

s1=Student("vivek",123456,21)
s1.get_age()
s1.set_age(15)
s1.get_age()