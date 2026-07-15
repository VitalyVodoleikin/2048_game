import pygame

import json
import os
import sys

from database import get_best, cur, insert_result
from logics import *

# ==========>>>>>>>>>>
# Константы
# ----------

GAMERS_DB = get_best()

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
COLOR_TEXT = (255, 127, 0)  # Цвет текста информационного табло

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


def init_const():
    """
    Функция инициализации констант и переменных.
    """

    global score, mas

    mas = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    # Поиск всех пустых клеток
    empty = get_empty_list(mas)
    # Перемешиваем список пустых клеток для последующей выборки случайной клетки
    random.shuffle(empty)
    # Выбираем случайные клетки
    random_num1 = empty.pop()
    random_num2 = empty.pop()
    # Получение координат выбранных случайных клеток
    x1, y1 = get_index_from_number(random_num1)
    x2, y2 = get_index_from_number(random_num2)
    # Присваиваем выбранным ячейкам по координатам случайным образом числа "2" или "4"
    # Получаем обновленный массив
    mas = insert_2_or_4(mas, x1, y1)
    mas = insert_2_or_4(mas, x2, y2)
    # Обнуление счета
    score = 0


def draw_top_gamers():
    """
    Функция вывода списка лучших игроков и их рекордов на информационное табло.
    """
    font_top = pygame.font.SysFont("comicsansms", 18)
    font_gamer = pygame.font.SysFont("comicsansms", 14)
    text_head = font_top.render("Best tries: ", True, COLOR_TEXT)
    screen.blit(text_head, (280, 5))
    for index, gamer in enumerate(GAMERS_DB):
        name, score = gamer
        s = f"{index + 1}. {name} - {score}"
        text_gamer = font_gamer.render(s, True, COLOR_TEXT)
        screen.blit(text_gamer, (280, 35 + 25 * index))
        print(index, name, score)


def draw_interface(score, delta=0):
    """
    Функция отрисовки интерфейса.

    ==========
    В последующем - разнести константы в отдельный файл, а после этого: эту функцию - в файл с логикой.
    """
    pygame.draw.rect(screen, WHITE, TITLE_REC)  # Отрисовка информационного табло
    font = pygame.font.SysFont("comicsansms", 50)  # Задание шрифта для клетки

    # Вывод информации на табло
    font_score = pygame.font.SysFont("comicsansms", 38)
    font_delta = pygame.font.SysFont("comicsansms", 22)
    text_score = font_score.render("Score: ", True, COLOR_TEXT)
    text_score_value = font_score.render(f"{score}", True, COLOR_TEXT)
    screen.blit(text_score, (20, 35))
    screen.blit(text_score_value, (175, 35))
    if delta > 0:  # Если очки за ход набраны, то отображаем их
        text_delta = font_delta.render(f"+{delta}", True, COLOR_TEXT)
        screen.blit(text_delta, (170, 75))

    # Вывод массива в консоль
    pretty_print(mas)

    # Вывод списка лучших игроков на информационном табло
    draw_top_gamers()

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


def draw_intro():
    """
    Функция отрисовки начальной заставки:
    - логотип;
    - текст приветствия;
    - запрос имени пользователя.
    """

    img2048 = pygame.image.load("2048.png")
    font = pygame.font.SysFont("comicsansms", 50)  # Задание шрифта для клетки
    text_welcome = font.render("Welcome!", True, WHITE)
    name = "Введите имя"
    is_find_name = False  # Внесено ли имя игрока на экране приветствия
    while not is_find_name:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Закрытие окна программы
                pygame.quit()  # Окончание игры
                sys.exit(0)  # Закрытие окна
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    if name == "Введите имя":
                        name = event.unicode
                    else:
                        name += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(name) > 2:
                        global USERNAME
                        USERNAME = name
                        is_find_name = True
                        break

        screen.fill(BLACK)  # Перезаливка экрана

        text_name = font.render(name, True, WHITE)  # Текст имени игрока
        # Вычисление координат текста с именем игрока
        rect_name = text_name.get_rect()
        rect_name.center = screen.get_rect().center

        # Прикрепление изображения лого и текст приветствия к экрану
        screen.blit(pygame.transform.scale(img2048, [200, 200]), [10, 10])
        screen.blit(text_welcome, (235, 90))
        screen.blit(text_name, rect_name)
        pygame.display.update()
    screen.fill(BLACK)  # Перезаливка экрана


def draw_game_over():
    """
    Функция отрисовки экрана после окончания игры.
    """

    global USERNAME, mas, score, GAMERS_DB

    img2048 = pygame.image.load("2048.png")
    font = pygame.font.SysFont("comicsansms", 30)  # Задание шрифта для клетки
    text_game_over = font.render("Game over!", True, WHITE)
    text_score = font.render(f"Вы набрали {score}", True, WHITE)
    best_score = GAMERS_DB[0][1]
    if score > best_score:
        text = "Рекорд побит!"
    else:
        text = f"Рекорд {best_score} не побит!"
    text_record = font.render(text, True, WHITE)

    # Сохранение результата игры в БД
    insert_result(USERNAME, score)

    # Обновление списка рекордов
    GAMERS_DB = get_best()

    make_disicion = False  # Решение о перезапуске игры
    while not make_disicion:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Закрытие окна программы
                pygame.quit()  # Окончание игры
                sys.exit(0)  # Закрытие окна
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Запуск игры с текущим именем игрока
                    make_disicion = True
                    init_const()
                elif event.key == pygame.K_RETURN:  # Запуск игры с новым именем игрока
                    USERNAME = None
                    make_disicion = True
                    init_const()

        screen.fill(BLACK)  # Перезаливка экрана
        screen.blit(pygame.transform.scale(img2048, [200, 200]), [10, 10])
        screen.blit(text_game_over, (235, 90))
        screen.blit(text_score, (40, 250))
        screen.blit(text_record, (40, 300))
        pygame.display.update()
    screen.fill(BLACK)


def save_game():
    data = {
        "user": USERNAME,
        "score": score,
        "mas": mas
    }
    with open("data.txt", "w") as outfile:
        json.dump(data, outfile)


def game_loop():
    """
    Функция основного цикла игры.
    """

    global score, mas

    # Отрисовка интерфейса
    draw_interface(score)
    # Обновление экрана
    pygame.display.update()

    was_mas_move = False  # Нажата ли нужная кнопка

    while is_zero_in_mas(mas) or can_move(mas):  # Если есть пустые клетки или можно сложить клетки
        # Основной цикл игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Закрытие окна программы

                # Сохранение игры
                save_game()

                pygame.quit()  # Окончание игры
                sys.exit(0)  # Закрытие окна

            elif event.type == pygame.KEYDOWN:  # При нажатии на кнопки
                delta = 0  # Счет очков
                if event.key == pygame.K_LEFT:  # Отрабатываем нажатие кнопки "Влево"
                    mas, delta, was_mas_move = move_left(mas)
                elif event.key == pygame.K_RIGHT:  # Отрабатываем нажатие кнопки "Вправо"
                    mas, delta, was_mas_move = move_right(mas)
                elif event.key == pygame.K_UP:  # Отрабатываем нажатие кнопки "Вверх"
                    mas, delta, was_mas_move = move_up(mas)
                elif event.key == pygame.K_DOWN:  # Отрабатываем нажатие кнопки "Вниз"
                    mas, delta, was_mas_move = move_down(mas)

                score += delta  # Увеличение счета очков

                if is_zero_in_mas(mas) and was_mas_move:  # Если еще есть ходы
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

                    was_mas_move = False  # Обнуляем условие нажание нужной кнопки

                # Отрисовка интерфейса
                draw_interface(score, delta)
                # Обновление экрана
                pygame.display.update()

        # print(USERNAME)  # Отладочный принт


# Задаем настройки: массив, очки, имя игрока
mas = None
score = None
USERNAME = None

# Проверка наличия результатов сохранения игры
path = os.getcwd()
# Если файл с сохраненными результатами есть,
# считываем данные из файла, удаляем файл сохранения
# и продолжаем игру с сохраненного места
if "data.txt" in os.listdir():
    with open("data.txt") as file:
        data = json.load(file)
        # print(data)  # Технический принт
        mas = data['mas']
        score = data['score']
        USERNAME = data['user']
    full_path = os.path.join(path, "data.txt")
    os.remove(full_path)
# Если файла с настройками нет,
# инициализируем новую игру
else:
    init_const()

# print("Список пустых клеток:", get_empty_list(mas))
# pretty_print(mas)

# for gamer in get_best():
#     print(gamer)


# Инициализация всех компонентов игры
pygame.init()
# Создание игрового окна с необходимыми размерами
screen = pygame.display.set_mode((WIDTH, HEIGTH))
# Создание заголовка окна для игры: "2048"
pygame.display.set_caption("2048")

while True:
    if USERNAME is None:
        # Отрисовка начальной заставки
        draw_intro()
    # Запуск основного цикла игры
    game_loop()
    # Отрисовка экрана окончания игры
    draw_game_over()
