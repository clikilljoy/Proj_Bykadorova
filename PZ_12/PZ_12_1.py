'''
Организовать и вывести последовательность из N случайных целых чисел. Из
исходной последовательности организовать первую последовательность, содержащую
числа кратные трем, и вторую – для всех остальных. Найти количество элементов в
полученных последовательностях.
'''
import random

def split_sequence(N):
    # Генерация последовательности из N случайных чисел
    sequence = [random.randint(1, 100) for _ in range(N)]
    print("Исходная последовательность:", sequence)
    
    # Разделение на числа кратные 3 и остальные
    multiples_of_3 = [num for num in sequence if num % 3 == 0]
    others = [num for num in sequence if num % 3 != 0]
    
    print("Числа кратные 3:", multiples_of_3)
    print("Остальные числа:", others)
    print("Количество чисел кратных 3:", len(multiples_of_3))
    print("Количество остальных чисел:", len(others))

N = 10
split_sequence(N)