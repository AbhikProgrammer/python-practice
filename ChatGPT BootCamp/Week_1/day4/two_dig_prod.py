import random

i = int(input("How many Multiplications do u wanna practise?   "))
x = random.randint(10, 99)
y = random.randint(10, 99)

score = 0

for r in range (i):
    x = random.randint(10, 99)
    y = random.randint(10, 99)


    prod = int(input("What is "+str(x)+"x"+str(y)+"?"))
    if prod == x*y:
        print("Correct")
        score = score + 1
        
    else:
        print("Incorrect")

print("You achieved, "+str(score)+"/"+str(i))
