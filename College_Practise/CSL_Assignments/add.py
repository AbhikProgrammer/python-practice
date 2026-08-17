x = [8, 9, 7]
y = [2, 7, 8, 8, 3, 1, 4]
sum = []
carry = 0

if len(x)>len(y):
    max = x
    min = y
else:
    max = y
    min = x

max.insert(0, 0)

for i in range(1, len(max)-len(min)+1):
    min.insert(0, 0)

print(max, min)

for i in range(0, len(max)):
    pos = len(max)-i-1
    x = max[pos]+min[pos]
    sum.insert(0, int(carry + x%10))
    carry = (x-x%10)/10

print(sum)
