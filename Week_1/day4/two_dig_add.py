import random

i = int(input("How many Multiplications do u wanna practise?   "))
x = random.randint(10, 99)
y = random.randint(10, 99)

for r in range (i):
    x = random.randint(10, 99)
    y = random.randint(10, 99)

    while True:
        prod = int(input("What is "+str(x)+"x"+str(y)+"?"))
        if prod == x*y:
            print("Correct")
            break
        else:
            print("Incorrect")
