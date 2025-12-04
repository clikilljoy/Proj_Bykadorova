'''
Вар 3
Из исходного текстового файла (hotline.txt) перенести в первый файл строки с
корректными номерами телефонов (т.е. в номере должно быть 11 цифр, например,
86532547891), а во второй с некорректными номерами телефонов. Посчитать
полученные строки в каждом файле.
'''
import re
import os

def create_hotline_file():

    content = """
  «Горячая линия» по вопросам оплаты труда - 8(863)269-58-17
«Горячая линия» по вопросам порядка начисления вознаграждения классным руководителям - 8632695817
«Горячая линия» по содержательным вопросам классного руководства - 8(863)267-05-88
«Горячая линия» по вопросам организации питания - 8632404656
«Горячая линия» ЕГЭ (по вопросам организации и проведения государственной итоговой аттестации) - 88632695742
«Горячая линия» ЕГЭ (по вопросам нарушения порядка проведения ГИА) - 8(863)82-22-03
«Горячая линия» по вопросам законности взимания платежей в общеобразовательных и дошкольных образовательных учреждениях - 88632822203
«Горячая линия» по вопросам приема в  учреждения среднего профессионального образования Ростовской области - 8863404950
«Телефон доверия» для студентов учреждений среднего профессионального образования Ростовской области - 88632404950
«Горячая линия» по вопросам опеки и попечительства в отношении несовершеннолетних - 886324049-47
«Горячая линия» по вопросу получения образования детьми с ограниченными возможностями здоровья и детьми-инвалидами - 88632404656
«Стоп, коррупция!» - 8(863)240-67-96
"""
    with open('hotline.txt', 'w', encoding='utf-8') as f:
        f.write(content)

def extract_digits(s):
    """Извлекает все цифры из строки и возвращает строку из цифр."""
    return ''.join(re.findall(r'\d', s))

def main():
    input_filename = 'hotline.txt'
    correct_filename = 'correct.txt'
    incorrect_filename = 'incorrect.txt'
    
    # Если файла hotline.txt нет, создаем его
    if not os.path.exists(input_filename):
        create_hotline_file()
    
    with open(input_filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    correct_count = 0
    incorrect_count = 0
    correct_lines = []
    incorrect_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:  # Пропускаем пустые строки
            continue
        
        digits = extract_digits(line)
        
        # Проверяем, есть ли цифры в строке
        if digits:
            if len(digits) == 11:  # Корректный номер - ровно 11 цифр
                correct_lines.append(line)
                correct_count += 1
            else:  # Некорректный номер - не 11 цифр
                incorrect_lines.append(line)
                incorrect_count += 1
        # Если цифр нет, строку игнорируем
    
    # Записываем корректные строки в файл
    with open(correct_filename, 'w', encoding='utf-8') as f:
        for line in correct_lines:
            f.write(line + '\n')
    
    # Записываем некорректные строки в файл
    with open(incorrect_filename, 'w', encoding='utf-8') as f:
        for line in incorrect_lines:
            f.write(line + '\n')
    
    # Выводим результаты
    print("=" * 50)
    print("РЕЗУЛЬТАТЫ ОБРАБОТКИ ФАЙЛА hotline.txt")
    print("=" * 50)
    print(f"Количество корректных номеров (11 цифр): {correct_count}")
    print(f"Количество некорректных номеров: {incorrect_count}")
    print(f"Корректные номера записаны в файл: {correct_filename}")
    print(f"Некорректные номера записаны в файл: {incorrect_filename}")
    
    # Выводим примеры найденных номеров
    if correct_lines:
        print(f"\nПример корректного номера: {extract_digits(correct_lines[0])}")
    if incorrect_lines:
        print(f"Пример некорректного номера: {extract_digits(incorrect_lines[0])} (длина: {len(extract_digits(incorrect_lines[0]))} цифр)")

if __name__ == '__main__':
    main()