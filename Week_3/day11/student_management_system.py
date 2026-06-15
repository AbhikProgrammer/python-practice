students = []

class Student:
    def __init__(self, name, branch, cgpa):
        self.name = name
        self.branch = branch
        self.cgpa = cgpa

    def display(self):
        print("\nName: ", self.name)
        print("Branch: ", self.branch)
        print("CGPA: ", self.cgpa)

num = int(input("Give number of students:   "))

for i in range(num):
    name = input("\nGive name of student " + str(i+1) + ":  ")
    branch = input("Give branch of student " + str(i+1) + ":  ")
    cgpa = input("Give CGPA of student " + str(i+1) + ":  ")

    student = Student(name, branch, cgpa)

    students.append(student)

for student in students:
    student.display()
