text = input("Введите список цифр : ")
list = text.split(" ")
#print(lst)

def max_min_replace(list):
    index_min = list.index(min(list))
    index_max = list.index(max(list))
    list[index_min], list[index_max] = list[index_max], list[index_min]
    return list
#max_min_replace(list)
print("Ваш список, в котором поменяны местами минимальный и максимальный элементы \n", max_min_replace(list))