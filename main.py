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
BLACK = (0, 0, 0)  # Цвет шрифта
# GRAY = (130, 130, 130)  # Цвет заливки пустого поля
WHITE = (255, 255, 255)

COLORS = {
    0: (130, 130, 130),
    2: (255, 255, 255),
    4: (255, 255, 125),
    8: (255, 255, 0),
    16: (255, 125, 255),
    32: (255, 125, 125),
    64: (255, 125, 0),
    128: (255, 0, 255),
    256: (255, 0, 125),
    512: (255, 0, 0),
    1024: (125, 255, 255),
    2048: (125, 255, 125)
}


# <<<<<<<<<<==========


def draw_interface():
    """
    Функция отрисовки интерфейса.

    ==========
    В последующем - разнести константы в отдельный файл, а после этого: эту функцию - в файл с логикой.
    """
    pygame.draw.rect(screen, WHITE, TITLE_REC)  # Отрисовка информационного табло
    font = pygame.font.SysFont("stxingkai", 70)  # Задание шрифта для клетки

    # Вывод массива в консоль
    pretty_print(mas)

    # Отрисовка клеток поля
    for row in range(BLOCKS):
        for column in range(BLOCKS):

            value = mas[row][column]  # Значение элемента массива
            text = font.render(f"{value}", True, BLACK)  # Отображение элемента массива

            w = column * SIZE_BLOCK + (column + 1) * MARGIN
            h = row * SIZE_BLOCK + (row + 1) * MARGIN + SIZE_BLOCK
            pygame.draw.rect(screen, COLORS[value], (w, h, SIZE_BLOCK, SIZE_BLOCK))

            if value != 0:  # Отрисовка числа, не равного "0"
                font_w, font_h = text.get_size()
                text_x = w + (SIZE_BLOCK - font_w) / 2

                text_y = h + (SIZE_BLOCK - font_h) / 2
                screen.blit(text, (text_x, text_y))


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
# Отрисовка интерфейса
draw_interface()
# Обновление экрана
pygame.display.update()

while is_zero_in_mas(mas):
    # Основной цикл игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Закрытие окна программы
            pygame.quit()  # Окончание игры
            sys.exit(0)  # Закрытие окна

        elif event.type == pygame.KEYDOWN:  # При нажатии на кнопки

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

            # Техниечский print
            print(f"Мы заполнили элемент под номером {random_num}")

            # Отрисовка интерфейса
            draw_interface()
            # Обновление экрана
            pygame.display.update()
