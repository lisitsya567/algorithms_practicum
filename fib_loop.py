import time

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

values = [3, 7, 12, 20, 24]

for n in values:
    start_time = time.time()
    result = fib(n)
    end_time = time.time()

    final_time = (end_time - start_time) * 1000
    print(f"fib({n}) = {result}, {final_time:.2f} мс")
