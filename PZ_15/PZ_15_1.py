'''
Вар 3
Приложение КАФЕДРА для автоматизации работы отдела кадров ВУЗа. Таблица
Преподавательский состав должна содержать следующие данные: Табельный номер,
Фамилия И.О., Дата рождения, Должность, Ученая степень, Нагрузка, Зарплата.
'''
import sqlite3
from sqlite3 import Error


DB_NAME = "kafedra.db"


def create_connection():
    try:
        conn = sqlite3.connect(DB_NAME)
        return conn
    except Error as e:
        print(f"Ошибка подключения: {e}")
    return None


def create_table(conn):
    """Создание таблицы преподавательского состава"""
    try:
        sql = """
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tabel_number TEXT NOT NULL,
            full_name TEXT NOT NULL,
            birth_date TEXT NOT NULL,
            position TEXT NOT NULL,
            academic_degree TEXT NOT NULL,
            workload INTEGER NOT NULL,
            salary REAL NOT NULL,
            phone TEXT,
            email TEXT
        );
        """
        conn.execute(sql)
        conn.commit()
    except Error as e:
        print(f"Ошибка создания таблицы: {e}")

def add_teacher(conn, data):
    try:
        sql = """
        INSERT INTO teachers
        (tabel_number, full_name, birth_date, position,
         academic_degree, workload, salary, phone, email)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        conn.execute(sql, data)
        conn.commit()
        print("Запись добавлена.")
    except Error as e:
        print(f"Ошибка вставки: {e}")

def search_teacher(conn):
    print("\nПоиск преподавателя:")
    print("1 — по фамилии")
    print("2 — по табельному номеру")
    print("3 — по должности")

    choice = input("Выберите вариант: ")

    if choice == "1":
        key = input("Введите фамилию или её часть: ")
        sql = "SELECT * FROM teachers WHERE full_name LIKE ?"
        params = (f"%{key}%",)

    elif choice == "2":
        key = input("Введите табельный номер: ")
        sql = "SELECT * FROM teachers WHERE tabel_number = ?"
        params = (key,)

    elif choice == "3":
        key = input("Введите должность: ")
        sql = "SELECT * FROM teachers WHERE position = ?"
        params = (key,)

    else:
        print("Неверный выбор.")
        return

    try:
        cur = conn.execute(sql, params)
        rows = cur.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("Ничего не найдено.")
    except Error as e:
        print(f"Ошибка поиска: {e}")

def delete_teacher(conn):
    print("\nУдаление преподавателя:")
    print("1 — по ID")
    print("2 — по табельному номеру")
    print("3 — по фамилии")

    choice = input("Выберите вариант: ")

    if choice == "1":
        key = input("ID: ")
        sql = "DELETE FROM teachers WHERE id = ?"
        params = (key,)

    elif choice == "2":
        key = input("Табельный номер: ")
        sql = "DELETE FROM teachers WHERE tabel_number = ?"
        params = (key,)

    elif choice == "3":
        key = input("Фамилия или часть: ")
        sql = "DELETE FROM teachers WHERE full_name LIKE ?"
        params = (f"%{key}%",)

    else:
        print("Неверный выбор.")
        return

    try:
        conn.execute(sql, params)
        conn.commit()
        print("Удаление выполнено.")
    except Error as e:
        print(f"Ошибка удаления: {e}")

def update_teacher(conn):
    print("\nРедактирование:")
    print("1 — обновить по ID")
    print("2 — обновить по табельному номеру")
    print("3 — обновить по фамилии")
    choice = input("Выберите вариант: ")

    new_salary = input("Введите новую зарплату: ")

    if choice == "1":
        key = input("ID: ")
        sql = "UPDATE teachers SET salary = ? WHERE id = ?"
        params = (new_salary, key)

    elif choice == "2":
        key = input("Табельный номер: ")
        sql = "UPDATE teachers SET salary = ? WHERE tabel_number = ?"
        params = (new_salary, key)

    elif choice == "3":
        key = input("Фамилия или часть: ")
        sql = "UPDATE teachers SET salary = ? WHERE full_name LIKE ?"
        params = (new_salary, f"%{key}%")

    else:
        print("Неверный выбор.")
        return

    try:
        conn.execute(sql, params)
        conn.commit()
        print("Запись обновлена.")
    except Error as e:
        print(f"Ошибка обновления: {e}")

def main():
    conn = create_connection()
    if conn is None:
        return

    create_table(conn)

    while True:
        print("\n=== МЕНЮ ===")
        print("1 — Добавить запись")
        print("2 — Поиск")
        print("3 — Удаление")
        print("4 — Редактирование")
        print("0 — Выход")

        choice = input("Выберите пункт: ")

        if choice == "1":
            data = (
                input("Табельный номер: "),
                input("ФИО: "),
                input("Дата рождения: "),
                input("Должность: "),
                input("Учёная степень: "),
                int(input("Нагрузка: ")),
                float(input("Зарплата: ")),
                input("Телефон: "),
                input("Email: "),
            )
            add_teacher(conn, data)

        elif choice == "2":
            search_teacher(conn)

        elif choice == "3":
            delete_teacher(conn)

        elif choice == "4":
            update_teacher(conn)

        elif choice == "0":
            conn.close()
            print("Выход.")
            break

        else:
            print("Неверный пункт меню.")


if __name__ == "__main__":
    main()