def fib_eo(n):

    a, b = 0, 1

    for _ in range(2, n + 1):
        a, b = b, (a + b) % 10

    if b % 2 == 0:
        print("even")
    else:
        print("odd")

n = int(input("Число:"))
print(fib_eo(n))
