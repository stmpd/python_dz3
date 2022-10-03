
#Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#in
#4
#out
#[2, 5, 8, 10]
#[20, 40]

from random import randrange


def create_new_list(count):
    lst = []
    for i in range(count):
        lst.append(randrange(10))
    print(lst)
    return lst


def opposite_sum(count, list_num):
    middle = count // 2
    res = []

    for i in range(middle):
        res.append(list_num[i] + list_num[count - i - 1])

    if count % 2 != 0:
        res.append(list_num[middle])

    return res


num = int(input('Введите число: '))
list = create_new_list(num)
print(opposite_sum(num, list))