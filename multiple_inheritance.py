# TWO PARENT CLASS , FROM PARENT CLASSES ONE CHILD CLASS
 # One child → multiple parents
class Teacher:
    def __init__(self):
        self.t_name="vivek"
        self.t_id=624
    def subject(self):
        return "Python"
    def back_ground(self):
        print(" Computer Science Engineering...!")

class Assisstant_Teacher:
    def __init__(self):
        print("calling from the Assisstant_Teacher")
    def subject(self):
        print("i will teach java")
    def back_ground(self):
        print("Computer Science Engineering...!")

class Inspired_Teacher(Teacher,Assisstant_Teacher):
    def __init__(self,ur_name,ur_id,subject,bg):
        self.name=ur_name
        self.id=ur_id
        self.t_subject=subject
        self.bg=bg
    def subject(self):
        Assisstant_Teacher().subject()
        print("i will teach C language")
    def work(self):
        print("i can teach")

    def display(self):
        print(f"I'm {self.name} , my ID is {self.id} and i will teach {self.t_subject}. My Back ground is {self.bg}")    

result_1=Inspired_Teacher("Vivek",6242,"PYTHON","Computer Science Engineering...!")
print(result_1.name)
print(result_1.id)
#print(result_1.__init__)
result_1.subject() 
#result_1.lesson()
#result_1.work()
result_1.display()




               