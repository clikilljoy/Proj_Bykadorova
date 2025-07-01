'''
Вар 3
Создайте класс «Счетчик», который имеет атрибут текущего значения и методы для
инкремента и декремента значения.
'''
class Counter:
    def __init__(self, initial_value=0):
        """Инициализация счетчика с начальным значением (по умолчанию 0)."""
        self.value = initial_value

    def increment(self, step=1):
        """Увеличивает значение счетчика на заданный шаг (по умолчанию 1)."""
        self.value += step

    def decrement(self, step=1):
        """Уменьшает значение счетчика на заданный шаг (по умолчанию 1)."""
        self.value -= step

    def get_value(self):
        """Возвращает текущее значение счетчика."""
        return self.value

    def __str__(self):
        """Возвращает строковое представление счетчика."""
        return f"Текущее значение счетчика: {self.value}"


if name == "__main__":
    counter = Counter()  # Создаем счетчик со значением 0
    print(counter)

    counter.increment()  # Увеличиваем на 1
    print(counter)

    counter.increment(3)  # Увеличиваем на 3
    print(counter)

    counter.decrement(2)  # Уменьшаем на 2
    print(counter)

    print("Текущее значение:", counter.get_value())