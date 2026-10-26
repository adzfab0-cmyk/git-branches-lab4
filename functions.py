"""Функции обработки массива (вариант 3: функции 3, 5, 12, 19, 31)."""

import numpy as np


# Cyrillic letters that look like Latin ones (the user may type them).
LATIN_ALIASES = {"а": "a", "с": "c", "е": "e"}


def not_implemented(matrix):
    """Placeholder for functions that are not written yet."""
    print("Эта функция пока не реализована.")


def show_negative_indices(matrix):
    """Function 3: print the indices of all negative elements."""
    rows, cols = np.where(matrix < 0)
    if rows.size == 0:
        print("Отрицательных элементов в массиве нет.")
        return
    print("Отрицательные элементы (индексы с нуля):")
    for i, j in zip(rows, cols):
        print(f"  [{i}][{j}] = {matrix[i, j]}")


FUNCTIONS = {
    "a": (
        "Индексы отрицательных элементов массива (функция 3)",
        show_negative_indices,
    ),
    "b": (
        "Элементы, кратные 5, и их индексы (функция 5)",
        not_implemented,
    ),
    "c": (
        "Количество положительных элементов выше главной диагонали "
        "(функция 12)",
        not_implemented,
    ),
    "d": (
        "Поменять местами первый и последний столбец (функция 19)",
        not_implemented,
    ),
    "e": (
        "Сумма положительных элементов в строках без нулей (функция 31)",
        not_implemented,
    ),
}


def wait_back():
    """Show the 'Back' item and wait until the user chooses it."""
    while input("\n0. Назад: ").strip() != "0":
        print("Ошибка: для возврата введите 0.")


def functions_menu(matrix):
    """Show the list of functions a-e and run the chosen one."""
    while True:
        print("\n=== Выполнение функций ===")
        for key, (title, _) in FUNCTIONS.items():
            print(f"{key}. {title}")
        print("0. Назад")
        choice = input("Выберите функцию: ").strip().lower()
        choice = LATIN_ALIASES.get(choice, choice)
        if choice == "0":
            return
        if choice in FUNCTIONS:
            print()
            FUNCTIONS[choice][1](matrix)
            wait_back()
        else:
            print("Ошибка: выберите a-e или 0.")
