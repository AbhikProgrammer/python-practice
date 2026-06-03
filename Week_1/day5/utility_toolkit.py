def square(a):
    return a*a

def cube(a):
    return a*a*a

def is_even(a):
    if a % 2 == 0:
        return True

    else:
        return False

def factorial(a):
    prod = 1

    for i in range(1, a+1):
        prod = prod * i

    return prod

a = int(input("Give the number:     "))

print("Square of the number is: ", square(a))
print("Cube of the number is: ", cube(a))
print("Even: ", is_even(a))
print("Factorial of number is: ", factorial(a))
