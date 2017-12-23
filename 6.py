import string

text = input("Введите вашу строку: ")

def is_isogramm():
    quantity_symbols = 0
    symbols = ""
    for i in text:
        if quantity_symbols > 0:
            print("Ваша строка не является изограммой", end="")
            return False

        if i in symbols and i != " ":
            quantity_symbols += 1
        symbols += i
    print("Ваша строка является изограммой", end="")
    return quantity_symbols == 0

is_isogramm()