class Student:
    def __init__(self, firstname, lastname, year=1, group ="A"):
        self.firstname = firstname
        self.lastname = lastname
        self.year = year
        self.group = group

    def __str__(self):
        return f"Student:{self.firstname} {self.lastname}"
    
    def __int__(self):
        return self.year
    
    def __bool__(self):
        return self.year > 1

student_1 = Student("Adam", "something")
student_2 = Student("joe", "Doe", 3)
#before
#print(f"Student:{student_1.firstname} {student_1.lastname}")
#print(f"Student:{student_2.firstname} {student_2.lastname}")
#after
print(student_1)
print(student_2)
print(int(student_1))
if student_2:
    print("student no longer in first class")
else:
    print("first year of student")