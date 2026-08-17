class Student:
    def __init__(self, name, branch, cgpa):
        self.name = name
        self.branch = branch
        self.cgpa = cgpa

    def display(self):
        print("\nStudent Details")
        print("Name:  ", self.name)
        print("Branch:  ", self.branch)
        print("CGPA:  ", self.cgpa)

student = Student(
    "Abhik",
    "Mechanical",
    8.5
)

student.display()
