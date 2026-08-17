students = {
    "Abhik": 15700,
    "Rahul": 9000,
    "Aman": 22000
}

for name, rank in students.items():
    print(name, "-", rank)

max = max(students.values())
min = min(students.values())

avg = sum(students.values())/3

print("Higest rank is", max)
print("Lowest rank is", min)

print("Average rank is", avg)

student = str(input("Give name of student:   "))
print("Rank of the student is:  ", students[student])
