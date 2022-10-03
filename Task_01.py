
#Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
#in
#5
#out
#[10, 2, 3, 8, 9]
#22


from random import randrange

def create_new_list(count):
    lst = []
    for i in range(count):
        lst.append(randrange(10))
    print(lst)
    return lst


def odd_sum(count, list_num):
    pos = 1
    result = 0
    while pos <= count:
        result += list_num[pos-1]
        pos += 2
    return result

num = int(input('Введите число: '))
list = create_new_list(num)
print(odd_sum(num, list))