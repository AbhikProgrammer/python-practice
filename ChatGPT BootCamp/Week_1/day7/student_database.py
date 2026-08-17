student = {}

student["name"] = input("Enter name:    ")
student["branch"] = input("Enter branch:    ")
student["cgpa"] = float(input("Enter CGPA:    "))

print("\n Student record")

for key, value in student.items():
    print(key, ":", value)
