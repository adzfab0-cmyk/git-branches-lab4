"""Функции обработки массива (вариант 3: функции 3, 5, 12, 19, 31)."""

import numpy as np

from array_io import show_array


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


def show_multiples_of_five(matrix):
    """Function 5: print elements divisible by 5 together with indices."""
    rows, cols = np.where(matrix % 5 == 0)
    if rows.size == 0:
        print("Элементов, кратных 5, в массиве нет.")
        return
    print("Элементы, кратные 5 (индексы с нуля):")
    for i, j in zip(rows, cols):
        print(f"  [{i}][{j}] = {matrix[i, j]}")


def count_positive_above_diagonal(matrix):
    """Function 12: count positive elements above the main diagonal."""
    upper = np.triu(matrix, k=1)
    count = int(np.count_nonzero(upper > 0))
    print("Количество положительных элементов выше главной диагонали:")
    print(count)


def swap_first_last_columns(matrix):
    """Function 19: swap the first and the last column (on a copy)."""
    result = matrix.copy()
    result[:, [0, -1]] = result[:, [-1, 0]]
    print("Исходный массив:")
    show_array(matrix)
    print("\nПосле обмена первого и последнего столбцов:")
    show_array(result)


def sum_positive_in_rows_without_zeros(matrix):
    """Function 31: sum positive elements of rows that have no zeros."""
    mask = ~np.any(matrix == 0, axis=1)
    rows_without_zeros = np.flatnonzero(mask)
    selected = matrix[mask]
    total = int(selected[selected > 0].sum())
    print(f"Строки без нулевых элементов: {rows_without_zeros.tolist()}")
    print(f"Сумма положительных элементов в этих строках: {total}")


FUNCTIONS = {
    "a": (
        "Индексы отрицательных элементов массива (функция 3)",
        show_negative_indices,
    ),
    "b": (
        "Элементы, кратные 5, и их индексы (функция 5)",
        show_multiples_of_five,
    ),
    "c": (
        "Количество положительных элементов выше главной диагонали "
        "(функция 12)",
        count_positive_above_diagonal,
    ),
    "d": (
        "Поменять местами первый и последний столбец (функция 19)",
        swap_first_last_columns,
    ),
    "e": (
        "Сумма положительных элементов в строках без нулей (функция 31)",
        sum_positive_in_rows_without_zeros,
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
