# Создать программу, выводящую на экран ближайшее к 10 из двух чисел, введенных пользователем.
# Например, среди чисел 8,5 и 11,45 ближайшее к десяти 11,45.

print("Программа будет выводить на экран ближайшее число к 10, из двух чисел введенных пользователем.")

first = float(input("Введите первое число: "))
second = float(input("Введите второе число: "))

if abs(10 - first) > abs(10 - second):
    print("Второе число %.2f  ближе к 10" % second)
else:
    print("Первое число %.2f ближе к 10" % first)