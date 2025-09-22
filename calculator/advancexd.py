def factorial(x):
    ad = 1
    for i in range(1, x+1):
        ad *= i
    return ad

def degree(x, y):
    z = x ** y
    return z