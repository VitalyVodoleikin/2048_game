import random


def pretty_print(mas):
    """
    Функция для удобного представления имеющегося массива.
    """
    print("-" * 10)
    print("Поле выглядит так:")
    for row in mas:
        print(*row)
    print("-" * 10)
    print()


def get_number_from_index(i, j):
    """
    Функция, которая возвращает порядковый номер клетки в массиве.

    ----------
    Цифра "4-ка" - это размерность массива.
    """
    return i * 4 + j + 1


def get_index_from_number(num):
    """
    Функция, которая возвращает координаты клетки по порядковому номеру клетки в массиве.
    """
    num -= 1
    x, y = num // 4, num % 4
    return x, y


def get_empty_list(mas):
    """
    Функция получения пустых клеток в массиве.

    ----------
    Цифра "4-ка" - это размерность массива.
    """
    empty = []  # Список пустых клеток
    for i in range(4):
        for j in range(4):
            if mas[i][j] == 0:
                num = get_number_from_index(i, j)
                empty.append(num)
    return empty


def insert_2_or_4(mas, x, y):
    """
    Функция заполнения масива числами "2" и "4" с вероятностью 0,75.
    """
    if random.random() <= 0.75:
        mas[x][y] = 2
    else:
        mas[x][y] = 4
    return mas


def is_zero_in_mas(mas):
    """
    Функция, для получения информации о том, есть ли пустые клетки в массиве.
    """
    for row in mas:
        if 0 in row:
            return True
    return False
