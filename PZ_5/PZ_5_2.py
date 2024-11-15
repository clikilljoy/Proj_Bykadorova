'''
Описать функцию TrianglePS(параметры), вычисляющую по стороне a
равностороннего треугольника его периметр P = 3*a и площадь S = a2 √3/4. С
помощью этой функции найти периметры и площади трех равносторонних
треугольников с данными сторонами.
'''
import math

def proverka_int(x):   # Проверка числа
    while type(x) != int:
        try:
            x = int(x)
            return x
        except ValueError:
            print('Вы ввели число не правильно')
            x = input('Повторите попытку: ')

def TrianglePS(x):
    P = 3 * x
    S = 2 * x * (math.sqrt(3)/4)
    return P, S

a = input('Введите сторону первого равносторонеено треугольника')
a = proverka_int(a)
b = input('Введите сторону второго равносторонеено треугольника')
b = proverka_int(b)
c = input('Введите сторону третьего равносторонеено треугольника')
c = proverka_int(c)

print(f'Периметр = {TrianglePS(a)[0]}, площадь = {TrianglePS(a)[1]}')
print(f'Периметр = {TrianglePS(b)[0]}, площадь = {TrianglePS(b)[1]}')
print(f'Периметр = {TrianglePS(c)[0]}, площадь = {TrianglePS(c)[1]}')