import random

list1 = [random.randint(-10,10) for i in range(5)]
print("Одномерный список случайных чисел: \n", list1)

list2 = [round(numeric/max([abs(i) for i in list1]),2) for numeric in list1]
max_number = max([abs(i) for i in list1])

list2 = [round((numeric/max_number),2) for numeric in list1]
print("Нормированный список: \n", list2)