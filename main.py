"""Главное меню программы для работы с двумерным массивом."""

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
    while True:
        print_menu()
        choice = input("Выберите пункт меню: ").strip()
        if choice == "1":
            print(STUB)  # size
        elif choice == "2":
            print(STUB)  # create
        elif choice == "3":
            print(STUB)  # view
        elif choice == "4":
            print(STUB)  # functions
        elif choice == "5":
            break  # exit
        else:
            print("Ошибка: выберите пункт от 1 до 5.")


if __name__ == "__main__":
    main()
