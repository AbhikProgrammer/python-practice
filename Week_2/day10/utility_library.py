def square(n):
    return n * n

def cube(n):
    return n * n * n

def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

def is_even(n):
    return n % 2 == 0
