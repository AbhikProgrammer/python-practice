x = float(input("Give weight in kilograms:   "))
y = float(input("Give height in metres:     "))

print("Your BMI is:  ", str(x/(y*y)))

if (x/(y*y))>18.5 and (x/(y*y))<24.9:
    print("You are healthy")

else:
    print("You are not healthy")
