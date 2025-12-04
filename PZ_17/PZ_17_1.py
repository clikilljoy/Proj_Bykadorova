'''
Вар 3
В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
приближенный к оригиналу (см. таблицу 1).
'''
import tkinter as tk

def check_even():
    txt = entry.get().strip()
    try:
        A = int(txt)
    except ValueError:
        result_value.config(text="Ошибка: введите целое число!", fg="red")
        return

    if A % 2 == 0:
        result_value.config(text=f"Число {A} — чётное.", fg="green")
    else:
        result_value.config(text=f"Число {A} — нечётное.", fg="blue")


root = tk.Tk()
root.title("Анкета Web-разработчика (адаптация под задачу)")

root.geometry("550x500")
root.resizable(False, False)

# ===== Заголовок =====
title = tk.Label(root, text="Анкета Web-разработчика", font=("Arial", 16, "bold"))
title.pack(pady=10)

# ===== Контейнер таблицы =====
table = tk.Frame(root, bd=2, relief="groove")
table.pack(padx=10, pady=10, fill="both")

# Цвета как на форме
left_bg  = "#e6e6e6"   # серая ячейка слева
right_bg = "#ffffff"   # белая справа


# === Строка 1 ===  (Регистрационное имя)
row1_l = tk.Label(table, text="Число A:", bg=left_bg, anchor="w", width=25, font=("Arial", 11), bd=1, relief="solid")
row1_l.grid(row=0, column=0, sticky="nsew")

entry = tk.Entry(table, bg=right_bg, font=("Arial", 11))
entry.grid(row=0, column=1, sticky="nsew", padx=2, pady=2)


# === Строка 2 ===  (Пароль)
row2_l = tk.Label(table, text="Проверка:", bg=left_bg, anchor="w", width=25, font=("Arial", 11), bd=1, relief="solid")
row2_l.grid(row=1, column=0, sticky="nsew")

check_btn = tk.Button(table, text="Проверить", font=("Arial", 11), command=check_even)
check_btn.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)


# === Строка 3 === (Подтверждение пароля)
row3_l = tk.Label(table, text="Результат:", bg=left_bg, anchor="w", width=25, font=("Arial", 11), bd=1, relief="solid")
row3_l.grid(row=2, column=0, sticky="nsew")

result_value = tk.Label(table, text="", bg=right_bg, anchor="w", font=("Arial", 11), bd=1, relief="solid")
result_value.grid(row=2, column=1, sticky="nsew", padx=2, pady=2)


# === Остальные строки — пустые, чтобы таблица была точно как на слайде ===
extra_labels = [
    "Ваша специализация:",
    "Пол:",
    "Ваши навыки:",
    "Дополнительные сведения о себе:"
]

for i, text in enumerate(extra_labels, start=3):
    lbl = tk.Label(table, text=text, bg=left_bg, anchor="w",
                   width=25, font=("Arial", 11), bd=1, relief="solid")
    lbl.grid(row=i, column=0, sticky="nsew")

    empty = tk.Label(table, text="", bg=right_bg, bd=1, relief="solid")
    empty.grid(row=i, column=1, sticky="nsew")


# === Две кнопки как внизу оригинальной таблицы ===
bottom = tk.Frame(root)
bottom.pack(pady=10)

reg_btn = tk.Button(bottom, text="зарегистрировать", font=("Arial", 12), width=20)
reg_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(bottom, text="очистить форму", font=("Arial", 12), width=20,
                      command=lambda: (entry.delete(0, tk.END), result_value.config(text="")))
clear_btn.grid(row=0, column=1, padx=10)

root.mainloop()