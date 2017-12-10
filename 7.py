# Найти сумму десяти первых чисел ряда Фибоначчи.
def fib(n):
    fib_list = []
    a, b = 0, 1
    for _ in range(0, n):
        fib_list += [b]
        a, b = b, a + b
    return fib_list

print("Первые 10 чисел ряда Фибоначчи: ", fib(10))
print("Сумма первых десяти чисел ряда Фибоначчи равна: ", sum(fib(10)))