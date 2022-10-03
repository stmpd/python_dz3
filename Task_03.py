
#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Без использования встроенной функции преобразования, без строк.
#in
#88
#out
#1011000



def binary(n):
    dig_list = []
    while n > 0:
        dig_list.append(n % 2)
        n = n // 2

    res = 0
    for i in range(len(dig_list)):
        res += dig_list[i] * (10 ** i)

    return res


num = int(input('Введите число: '))
print(binary(num))