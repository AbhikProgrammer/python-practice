def total(a, b, c):
    return a + b + c

def avrg(a, b, c):
    return (a + b + c)/3

def grade(a):
    if a > 50:
        return "Good grade"
    else:
        return "Somehow passed"

a = int(input("Give marks of student 1:     "))
b = int(input("Give marks of student 2:     "))
c = int(input("Give marks of student 3:     "))

print("Total marks:  ", total(a, b, c))
print("Average marks:   ", avrg(a, b, c))

sum = 1
for i in [a, b, c]:
    print("Grade of student "+str(sum)+"is: "+grade(i))
    sum = sum + 1
