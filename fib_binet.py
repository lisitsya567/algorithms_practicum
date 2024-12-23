import math

def fib(n):
    a = (1 + math.sqrt(5)) / 2
    b = (1 - math.sqrt(5)) / 2
    fib_n = (a ** n - b ** n) / math.sqrt(5)
    return round(fib_n)

n = 32
result = fib(n)
print(result)
