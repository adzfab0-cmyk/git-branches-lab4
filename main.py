"""Главное меню программы для работы с двумерным массивом."""

from array_io import ask_size, create_array_menu, show_array
from functions import functions_menu

STUB = "Этот пункт меню пока не реализован."


def print_menu():
    """Print the main menu."""
    print("\n=== Главное меню ===")
    print("1. Ввод размера массива")
    print("2. Создание массива")
    print("3. Просмотр созданного массива")
    print("4. Выполнение функций")
    print("5. Выход")


def main():
    """Run the main menu loop."""
    rows = cols = None
    matrix = None
    while True:
        print_menu()
        choice = input("Выберите пункт меню: ").strip()
        if choice == "1":
            rows, cols = ask_size()
            matrix = None
            print(f"Размер массива: {rows} (строк) x {cols} (столбцов).")
        elif choice == "2":
            if rows is None:
                print("Сначала задайте размер массива (пункт 1).")
            else:
                created = create_array_menu(rows, cols)
                if created is not None:
                    matrix = created
        elif choice == "3":
            if matrix is None:
                print("Массив ещё не создан (пункт 2).")
            else:
                show_array(matrix)
        elif choice == "4":
            if matrix is None:
                print("Массив ещё не создан (пункт 2).")
            else:
                functions_menu(matrix)
        elif choice == "5":
            break  # exit
        else:
            print("Ошибка: выберите пункт от 1 до 5.")


if __name__ == "__main__":
    main()
