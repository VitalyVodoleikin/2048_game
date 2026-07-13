import sys

import pygame

from logics import *

# ==========>>>>>>>>>>
# Константы
# ----------

# Размеры
BLOCKS = 4  # Размерность поля = 4х4
SIZE_BLOCK = 110  # Сторона блока в 110 пикселей
MARGIN = 10  # Отступ между блоками в 10 пикселей
WIDTH = BLOCKS * SIZE_BLOCK + (BLOCKS + 1) * MARGIN  # Ширина окна для игры
HEIGTH = WIDTH + 110  # Высота окна для игры + информационное табло в 110 пикселей
TITLE_REC = pygame.Rect(0, 0, WIDTH, SIZE_BLOCK)  # Информационное табло

# Цвета
WHITE = (255, 255, 255)
GRAY = (130, 130, 130)

# <<<<<<<<<<==========


# Предварительно, размерность масива будет 4х4 клетки
mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

mas[1][2] = 2
mas[3][0] = 4

print("Список пустых клеток:", get_empty_list(mas))
pretty_print(mas)

# Инициализация всех компонентов игры
pygame.init()

# Создание игрового окна с необходимыми размерами
screen = pygame.display.set_mode((WIDTH, HEIGTH))
# Создание заголовка окна для игры: "2048"
pygame.display.set_caption("2048")

while is_zero_in_mas(mas):
    # Основной цикл игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Закрытие окна программы
            pygame.quit()  # Окончание игры
            sys.exit(0)  # Закрытие окна

        elif event.type == pygame.KEYDOWN:  # При нажатии на кнопки
            pygame.draw.rect(screen, WHITE, TITLE_REC)  # Отрисовка элементов

            # Отрисовка клеток поля
            for row in range(BLOCKS):
                for column in range(BLOCKS):
                    w = column * SIZE_BLOCK + (column + 1) * MARGIN
                    h = row * SIZE_BLOCK + (row + 1) * MARGIN + SIZE_BLOCK
                    pygame.draw.rect(screen, GRAY, (w, h, SIZE_BLOCK, SIZE_BLOCK))

            # # Получение команды от пользователя
            # input()

            # Поиск всех пустых клеток
            empty = get_empty_list(mas)
            # Перемешиваем список пустых клеток для последующей выборки случайной клетки
            random.shuffle(empty)
            # Выбираем случайную клетку
            random_num = empty.pop()
            # Получение координат выбранной случайной клетки
            x, y = get_index_from_number(random_num)
            # Присваиваем выбранной ячейке по координатам случайным образом число "2" или "4"
            # Получаем обновленный массив
            mas = insert_2_or_4(mas, x, y)

            # Техниечские print-ы
            print(f"Мы заполнили элемент под номером {random_num}")
            pretty_print(mas)

    # Обновление экрана
    pygame.display.update()
