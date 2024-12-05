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

def sum_rad(x):
    i = 0
    while x != 0:
        i += x % 10
        x = x // 10
    return i

print(sum_rad(int(input("Введите числовой ряд: "))))
