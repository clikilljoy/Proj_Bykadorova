"""
Дано целое число N(>0). С помощью операций деления нацело и взятия остатка от деления определить, имеется ли в записи числа N цифра "2".
Если имеется, то вывести TRUE, если нет - вывести FALSE.
"""
def proverka_int(x):   # Проверка числа
    while type(x) != int:
        try:
            x = int(x)
            return x
        except ValueError:
            print('Вы ввели число не правильно')
            x = input('Повторите попытку: ')

n = input('Введите n ')
n = proverka_int(n)

digith = 0
k = 0
b = len(str(n))

while n != 0:
    digith = n % 10
    n = n // 10
    k += 1
    if digith == 2:
        print(True)
        break
    if k == b:
        print(False)