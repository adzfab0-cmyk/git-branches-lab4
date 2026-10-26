"""Ввод размера, создание и просмотр массива."""

import numpy as np


def read_int(prompt, min_value=None, max_value=None):
    """Read an integer from the user until the input is valid."""
    while True:
        text = input(prompt).strip()
        try:
            value = int(text)
        except ValueError:
            print("Ошибка: нужно ввести целое число.")
            continue
        if min_value is not None and value < min_value:
            print(f"Ошибка: число должно быть не меньше {min_value}.")
            continue
        if max_value is not None and value > max_value:
            print(f"Ошибка: число должно быть не больше {max_value}.")
            continue
        return value


def ask_size():
    """Ask the user for the array width and height.

    Returns:
        tuple: (rows, cols) - height and width of the array.
    """
    print("Введите размер двумерного массива (от 1 до 20).")
    cols = read_int("Количество элементов по ширине (столбцов): ", 1, 20)
    rows = read_int("Количество элементов по высоте (строк): ", 1, 20)
    return rows, cols


def create_manual(rows, cols):
    """Fill the array element by element, showing the index of each one."""
    matrix = np.zeros((rows, cols), dtype=int)
    for i in range(rows):
        for j in range(cols):
            matrix[i, j] = read_int(f"Элемент [{i}][{j}]: ")
    return matrix


def create_auto(rows, cols):
    """Fill the array with random integers from 0 to 100 inclusive."""
    return np.random.randint(0, 101, size=(rows, cols))


def create_array_menu(rows, cols):
    """Show the creation submenu.

    Returns:
        numpy.ndarray or None: the new array, or None if the user went back.
    """
    while True:
        print("\n--- Создание массива ---")
        print("1. Вручную")
        print("2. Автоматически (случайные числа от 0 до 100)")
        print("0. Назад")
        choice = input("Выберите вариант: ").strip()
        if choice == "1":
            matrix = create_manual(rows, cols)
            print("Массив создан.")
            return matrix
        if choice == "2":
            matrix = create_auto(rows, cols)
            print("Массив создан.")
            return matrix
        if choice == "0":
            return None
        print("Ошибка: выберите 1, 2 или 0.")


def show_array(matrix):
    """Print the array as an aligned table."""
    rows, cols = matrix.shape
    print(f"Массив {rows} x {cols}:")
    width = max(len(str(value)) for value in matrix.flat)
    for row in matrix:
        print(" ".join(str(value).rjust(width) for value in row))
