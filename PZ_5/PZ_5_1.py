'''
Вар 3
Составить функцию, которая выполнит суммирования числового ряда.
'''
def proverka_int(x):   # Проверка числа
    while type(x) != int:
        try:
            x = int(x)
            return x
        except ValueError:
            print('Вы ввели число не правильно')
            x = input('Повторите попытку: ')

def sum_digith(x):
    k = 0
    for i in str(x):
        k += int(i)
    return k

a = input('Введите числовой ряд: ')
a = proverka_int(a)
print(sum_digith(a))
