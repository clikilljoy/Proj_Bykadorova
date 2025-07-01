'''
Вар 3
Дана строка 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16',
отражающая продажи продукции по дням в кг. 
Преобразовать информацию из строки в словари, 
с использованием функции найти максимальные продажи по
каждому виду продукции, результаты вывести на экран. 
'''
def find_max_sales(sales_str):
    parts = sales_str.split()
    products = {}
    current_product = None
    
    for part in parts:
        if part.isalpha():
            # Если это название продукта
            current_product = part
            products[current_product] = []
        else:
            # Если это число продаж
            if current_product is not None:
                products[current_product].append(int(part))
    
    # Находим максимальные продажи для каждого продукта
    max_sales = {}
    for product, sales in products.items():
        max_sales[product] = max(sales)
    
    return max_sales

# Исходная строка
sales_string = 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16'

result = find_max_sales(sales_string)

for product, max_sale in result.items():
    print(f"Максимальные продажи {product}: {max_sale} кг")