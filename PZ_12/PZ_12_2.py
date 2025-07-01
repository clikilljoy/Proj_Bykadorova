'''
Вар 3
Составить генератор (yield), который выводит из строки только цифры.
'''
def extract_digits(text):
    for char in text:
        if char.isdigit():
            yield char

text = "a1b2c3d4e5f6"
digits = list(extract_digits(text))
print("Исходная строка:", text)
print("Извлеченные цифры:", digits)