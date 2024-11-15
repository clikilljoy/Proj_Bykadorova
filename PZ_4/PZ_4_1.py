"""
вар 3
Дано вещественное число - цена 1 кг конфет. Вывести стоимость 1, 2, ..., 10 кг конфет.
"""
def proverka_int(x):   # Проверка числа
    while type(x) != int:
        try:
            x = int(x)
            return x
        except ValueError:
            print('Вы ввели число не правильно')
            x = input('Повторите попытку: ')

price = input('Введите стоимость одного киллограма конфет: ')
price = proverka_int(price)


for i in range(1, 11):
    print('Стоимость конфет за', i, 'киллограм =', i * price)