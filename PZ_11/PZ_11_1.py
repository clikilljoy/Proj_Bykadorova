'''
Вар 3
Средствами языка Python сформировать текстовый файл (.txt), содержащий
последовательность из целых положительных и отрицательных чисел. Сформировать
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
обработку элементов:
Исходные данные:
Количество элементов:
Минимальный элемент:
Квадраты четных элементов:
Сумма квадратов четных элементов:
Среднее арифметическое суммы квадратов четных элементов
'''
# Создаем исходный файл с последовательностью чисел
with open('numbers.txt', 'w', encoding='utf-8') as f:
    # Генерируем последовательность положительных и отрицательных чисел
    numbers = [5, -3, 12, -7, 8, 2, -4, 15, -6, 9, 10, -1, 14, -9]
    # Записываем числа в файл через пробел
    f.write(' '.join(map(str, numbers)))

print("Исходные данные из файла numbers.txt:")
with open('numbers.txt', 'r', encoding='utf-8') as f:
    print(f.read())

# Читаем данные из файла
with open('numbers.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    # Преобразуем строку в список чисел
    numbers = list(map(int, data.split()))

# Выполняем требуемую обработку
# Количество элементов
count = len(numbers)

# Минимальный элемент
min_element = min(numbers)

# Квадраты четных элементов
even_squares = [x**2 for x in numbers if x % 2 == 0]

# Сумма квадратов четных элементов
sum_even_squares = sum(even_squares)

# Среднее арифметическое суммы квадратов четных элементов
# Делим на количество четных элементов
if even_squares:
    average_even_squares = sum_even_squares / len(even_squares)
else:
    average_even_squares = 0

# Записываем результат в новый файл
with open('result_1.txt', 'w', encoding='utf-8') as f:
    f.write("Исходные данные:\n")
    f.write(' '.join(map(str, numbers)) + '\n')
    f.write(f"Количество элементов: {count}\n")
    f.write(f"Минимальный элемент: {min_element}\n")
    f.write(f"Квадраты четных элементов: {' '.join(map(str, even_squares))}\n")
    f.write(f"Сумма квадратов четных элементов: {sum_even_squares}\n")
    f.write(f"Среднее арифметическое суммы квадратов четных элементов: {average_even_squares:.2f}\n")

print("\n" + "="*60)
print("Задание 1 выполнено!")
print("="*60)
print("Созданные файлы:")
print("1. numbers.txt - исходная последовательность чисел")
print("2. result_1.txt - результаты обработки")
print("\nСодержимое файла result_1.txt:")
print("="*40)
with open('result_1.txt', 'r', encoding='utf-8') as f:
    print(f.read())
print("="*40)