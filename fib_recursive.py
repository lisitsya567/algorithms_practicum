import time

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

values = [6, 10, 12, 20, 24]

for n in values:
    start_time = time.time()
    result = fib(n)
    end_time = time.time()

    final_time = (end_time - start_time) * 1000
    print(f"fib({n}) = {result}, {final_time:.2f} мс")
