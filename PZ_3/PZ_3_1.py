"""
вариант 3
Размер скидки на продукты определен следующим образом: при покупке до 500 р. 
скидка составит 2%; при покупке от 500 р. до 1000 р. скидка составит 3%; при покупке от 1000 р. до 1500 р. скидка составит 4%; 
при покупке от 1500 р. до 2000 р. скидка составит 5%. Составить программу определяющую размер скидки в зависимости от потраченной суммы.
"""
def proverka_float(x):   # Проверка числа
    while type(x) != float:
        try:
            x = float(x)
            return x
        except ValueError:
            print('Вы ввели число не правильно')
            x = input('Повторите попытку: ')

def calculate_discount(buy):
    if buy < 500:
        discount = 0.02
    elif 500 <= buy < 1000:
        discount = 0.03
    elif 1000 <= buy < 1500:
        discount = 0.04
    elif 1500 <= buy < 2000:
        discount = 0.05

    else:
        discount = 0

    return discount * 100
    
buy_spent = input("Введите сумму покупки: ")
buy_spent = proverka_float(buy_spent)
discount = calculate_discount(buy_spent)
print(f"Ваша скидка составляет {discount}%")