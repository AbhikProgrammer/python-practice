marks = []

for i in range(5):
    mark = int(input("Give the marks for Student "+str(i+1)+": "))
    marks.append(mark)

marks_high = max(marks)
marks_low = min(marks)
marks_avg = sum(marks)/5

print("Highest marks is, ", marks_high)
print("Lowest marks is, ", marks_low)
print("Average marks is, ", marks_avg)
