'''
Вар 3
Из матрицы сформировать массив из положительных четных элементов, найти их
сумму и среднее арифметическое.
'''
def process_positive_even_elements(matrix):
    """
    Формирует массив из положительных четных элементов матрицы,
    находит их сумму и среднее арифметическое
    
    Args:
        matrix: двумерный список (матрица)
    
    Returns:
        Кортеж: (массив положительных четных элементов, сумма, среднее)
    """
    # Формируем массив положительных четных элементов
    positive_even_elements = []
    for row in matrix:
        for element in row:
            if element > 0 and element % 2 == 0:  # Положительный и четный
                positive_even_elements.append(element)
    
    # Вычисляем сумму и среднее арифметическое
    if positive_even_elements:
        total_sum = sum(positive_even_elements)
        average = total_sum / len(positive_even_elements)
    else:
        total_sum = 0
        average = 0
    
    return positive_even_elements, total_sum, average


# Пример использования
if __name__ == "__main__":
    # Тестовая матрица
    test_matrix = [
        [2, -3, 4],
        [5, 6, -7],
        [8, 9, 10],
        [0, 12, -1]
    ]
    
    print("Исходная матрица:")
    for row in test_matrix:
        print(row)
    
    # Выполняем обработку
    positive_even, total, avg = process_positive_even_elements(test_matrix)
    
    print(f"\nМассив положительных четных элементов: {positive_even}")
    print(f"Количество элементов: {len(positive_even)}")
    print(f"Сумма положительных четных элементов: {total}")
    print(f"Среднее арифметическое: {avg:.2f}")
    
    # Тест с матрицей без положительных четных элементов
    print("\n" + "=" * 40)
    print("Тест с матрицей без положительных четных элементов:")
    
    test_matrix2 = [
        [-1, -3, -5],
        [1, 3, 5],
        [-2, -4, -6]
    ]
    
    print("Матрица:")
    for row in test_matrix2:
        print(row)
    
    positive_even2, total2, avg2 = process_positive_even_elements(test_matrix2)
    
    if positive_even2:
        print(f"\nМассив положительных четных элементов: {positive_even2}")
        print(f"Сумма: {total2}")
        print(f"Среднее: {avg2:.2f}")
    else:
        print("\nВ матрице нет положительных четных элементов")
        print(f"Сумма: {total2}")
        print(f"Среднее: {avg2:.2f}")