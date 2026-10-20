class Student :
    def __init__(self, name, id, grade):
        self.name= name 
        self.id= id
        self.grade= grade
    def show_student(self):
        print("Student Name:", self.name, "Student ID:", self.id, "Student Grade:", self.grade)
student1=Student("john", 3033, 98.0)
student2=Student("jessy", 3044, 97.0)
student1.show_student()
student2.show_student()
#vvv