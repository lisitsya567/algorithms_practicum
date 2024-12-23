def fib(n, memo=[0, 1]):
    if n < len(memo):
        return memo[:n + 1]

    memo.append(fib(n - 1, memo)[-1] + fib(n - 2, memo)[-1])
    return memo[:n + 1]

n = 8
result = fib(n)
print(result)
