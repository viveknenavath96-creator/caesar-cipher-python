# Hybrid = Combination of different inheritance types.

class University:
    def __init__(self,uni_name):
        self.uni_name=uni_name
    def show_details(self):
         print(f"university name : {self.uni_name}")

class Course(University):
    def __init__(self,course_name,uni_name):
        University.__init__(self,uni_name)
        self.course_name=course_name

    def show_details(self):
        University.show_details(self)
        print(f"course name : {self.course_name}")

class Branch(University):
    def __init__(self,branch_name,uni_name):
        University.__init__(self,uni_name)
        self.branch_name=branch_name

    def show_details(self):
        University.show_details(self)
        print(f" Branch name : {self.branch_name}")

class Student(Course,Branch):
    def __init__(self,student_name,course_name,branch_name,uni_name):
       Course.__init__(self,course_name,uni_name)
       Branch.__init__(self,branch_name,uni_name)
       self.student_name=student_name

    def show_details(self):
       Course.show_details(self)
       Branch.show_details(self)
       print(f"Student name : {self.student_name}")

class Faculty(Branch):
    def __init__(self,faculty_name,branch_name,uni_name):
        Branch.__init__(self,branch_name,uni_name)
        self.faculty_name=faculty_name

    def show_details(self):
        Branch.show_details(self)
        print(f"Faculty name : {self.faculty_name}")

# name_1=University("JNTUH")
# name_1.show_details()       

name_1=Student("VIVEK","ENGINEERING","CYBER SECURITY","jntuh")
name_1.show_details()