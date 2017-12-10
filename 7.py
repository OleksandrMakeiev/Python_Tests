def fib(n):
    fib_list = []
    a, b = 0, 1
    for _ in range(0, n):
        fib_list += [b]
        a, b = b, a + b
    return fib_list

print("Сумма первых десяти чисел ряда Фибаначи равна: ", sum(fib(10)))