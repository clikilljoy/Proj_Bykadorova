'''
Вар 3
В двумерном списке элементы на главной диагонали увеличить в 2 раза.
'''
"""
Задание 1: В двумерном списке элементы на главной диагонали увеличить в 2 раза
"""
"""
Задание 1: В двумерном списке элементы на главной диагонали увеличить в 2 раза
"""

def double_main_diagonal(matrix):
    """
    Увеличивает элементы на главной диагонали матрицы в 2 раза
    
    Args:
        matrix: двумерный список (матрица)
    
    Returns:
        Модифицированная матрица
    """
    for i in range(len(matrix)):
        if i < len(matrix[i]):  # Проверяем, что индекс не выходит за границы строки
            matrix[i][i] *= 2
    return matrix


# Пример использования
if __name__ == "__main__":
    # Тестовая матрица
    test_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("Исходная матрица:")
    for row in test_matrix:
        print(row)
    
    # Выполняем преобразование
    result_matrix = double_main_diagonal(test_matrix)
    
    print("\nМатрица после увеличения элементов главной диагонали в 2 раза:")
    for row in result_matrix:
        print(row)
    
    # Дополнительный тест с неквадратной матрицей
    print("\n" + "=" * 40)
    print("Тест с неквадратной матрицей 3x4:")
    
    test_matrix2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    
    print("Исходная матрица:")
    for row in test_matrix2:
        print(row)
    
    result_matrix2 = double_main_diagonal(test_matrix2)
    
    print("\nРезультат:")
    for row in result_matrix2:
        print(row)