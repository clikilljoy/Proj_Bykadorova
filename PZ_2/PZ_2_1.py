"""
вар 3
Скорость лодки в стоячей воде V км/ч, скорость течения реки U км/ч
(U < V). Время движения лодки по озеру T1 ч, а по реке (против течения) - Т2 ч.
Определить путь S, пройденный лодкой (путь = время * скорость). Учесть, что при движении против течения скорость лодки уменьшается на величину скорости течения.
"""
def proverka_float(x):   # Проверка числа
    while type(x) != float:
        try:
            x = float(x)
            return x
        except ValueError:
            print('Вы ввели число не правильно')
            x = input('Повторите попытку: ')

V = input("Введите скорость лодки в стоячей воде (км/ч): ")
V = proverka_float(V)

U = input("Введите скорость течения реки (км/ч): ")
U = proverka_float(U)

T1 = input("Введите время движения по озеру (часы): ")
T1 = proverka_float(T1)

T2 =input("Введите время движения по озеру против течения (часы): ")
T2 = proverka_float(T2)

if U < V:
    
    S1 = T1 * V
    print("Путь при условии лодки в стоячей воде и движение по течению ", S1)

    S2 = T2 * V
    print("Путь при условии лодки в стоячей воде и движение против течения ", S2)

    
else:
    print("Ошибка: Скорость течения должна быть меньше скорости лодки.")