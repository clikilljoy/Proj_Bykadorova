'''
Вар 3
Из предложенного текстового файла (text18-3.txt) вывести на экран его содержимое,
количество знаков пунктуации в первых четырёх строках. Сформировать новый файл, в
который поместить текст в стихотворной форме предварительно заменив символы третей
строки их числовыми кодами.
'''
# Создаем исходный файл с текстом стихотворения (по условию)
poem_lines = [
    "Мы долго молча отступали,",
    "Досадно было, боя ждали,",
    "Ворчали старики:",
    "«Что ж мы? на зимние квартиры?",
    "Не смеют, что ли, командиры",
    "Чужие изорвать мундиры",
    "О русские штыки?»"
]

with open('text18-3.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(poem_lines))

# Выводим содержимое файла на экран
print("Содержимое файла text18-3.txt:")
print("="*40)
with open('text18-3.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)
print("="*40)

# Подсчитываем количество знаков пунктуации в первых четырех строках
with open('text18-3.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
# Определяем знаки пунктуации
punctuation_marks = set('.,:;!?«»"\'—()-')
punctuation_count = 0

print("\nПодсчет знаков пунктуации в первых четырех строках:")
print("-"*50)
for i in range(min(4, len(lines))):
    line = lines[i].strip()
    line_punctuation = [char for char in line if char in punctuation_marks]
    count = len(line_punctuation)
    punctuation_count += count
    print(f"Строка {i+1}: '{line}'")
    print(f"  Знаков пунктуации: {count}")
    if line_punctuation:
        print(f"  Знаки: {', '.join(line_punctuation)}")
    print()

print(f"Общее количество знаков пунктуации в первых четырех строках: {punctuation_count}")

# Создаем новый файл с замененной третьей строкой
with open('text18-3_new.txt', 'w', encoding='utf-8') as f:
    for i, line in enumerate(lines, 1):
        if i == 3:  # Третья строка
            # Заменяем символы на их числовые коды (ASCII/Unicode)
            codes = ' '.join(str(ord(char)) for char in line.strip())
            f.write(codes + '\n')
        else:
            f.write(line)

print("\n" + "="*60)
print("Создан новый файл 'text18-3_new.txt'")
print("Третья строка заменена на числовые коды символов.")
print("\nСодержимое нового файла:")
print("="*40)
with open('text18-3_new.txt', 'r', encoding='utf-8') as f:
    print(f.read())
print("="*40)

# Дополнительная информация о третьей строке
print("\nДополнительная информация о третьей строке:")
third_line = lines[2].strip()  # Индексация с 0, поэтому третья строка - индекс 2
print(f"Исходная строка: '{third_line}'")
print("Коды символов:")
for i, char in enumerate(third_line):
    print(f"  '{char}' -> {ord(char)}")