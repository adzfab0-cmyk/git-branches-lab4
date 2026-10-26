"""Ввод размера, создание и просмотр массива."""


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
