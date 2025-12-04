'''
Вар 3
Разработать программу с применением пакета tk, взяв в качестве условия одну
любую задачу из ПЗ №№ 2 – 9. Дано целое число A. Проверить истинность высказывания: "Число A является четным".
'''
import tkinter as tk
from tkinter import messagebox

def check_even():
    try:
        A = int(entry.get())
        if A % 2 == 0:
            messagebox.showinfo("Результат", f"Число {A} является чётным.")
        else:
            messagebox.showinfo("Результат", f"Число {A} является нечётным.")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное целое число!")

# Создаем окно
window = tk.Tk()
window.title("Проверка чётности числа A")
window.geometry("300x150")

# Надпись
label = tk.Label(window, text="Введите целое число A:")
label.pack(pady=5)

# Поле ввода
entry = tk.Entry(window)
entry.pack(pady=5)

# Кнопка
button = tk.Button(window, text="Проверить", command=check_even)
button.pack(pady=10)

# Запуск приложения
window.mainloop()