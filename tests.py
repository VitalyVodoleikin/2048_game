import unittest
from logics import get_number_from_index, get_empty_list, get_index_from_number, \
    is_zero_in_mas, move_left, move_right, move_up, move_down, can_move


class Test_2048(unittest.TestCase):

    def test_1_get_number_from_index(self):
        """
        Тест получения порядкового номера клетки по координатам клетки массива.
        """
        self.assertEqual(get_number_from_index(1, 2), 7)

    def test_2_get_number_from_index(self):
        """
        Тест получения порядкового номера клетки по координатам клетки массива.
        """
        self.assertEqual(get_number_from_index(3, 3), 16)

    def test_3_get_empty_list(self):
        """
        Тест получения списка пустых клеток массива.
        """
        empty_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        mas = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(get_empty_list(mas), empty_list)

    def test_4_get_empty_list(self):
        """
        Тест получения списка пустых клеток массива.
        """
        empty_list = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        mas = [
            [2, 2, 2, 2],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(get_empty_list(mas), empty_list)

    def test_5_get_empty_list(self):
        """
        Тест получения списка пустых клеток массива.
        """
        empty_list = []
        mas = [
            [2, 2, 2, 2],
            [2, 4, 2, 4],
            [4, 2, 4, 2],
            [4, 4, 4, 4]
        ]
        self.assertEqual(get_empty_list(mas), empty_list)

    def test_6_get_index_from_number(self):
        """
        Тест получения координат клетки по порядковому номеру клетки массива.
        """
        self.assertEqual(get_index_from_number(7), (1, 2))

    def test_7_get_index_from_number(self):
        """
        Тест получения координат клетки по порядковому номеру клетки массива.
        """
        self.assertEqual(get_index_from_number(16), (3, 3))

    def test_8_get_index_from_number(self):
        """
        Тест получения координат клетки по порядковому номеру клетки массива.
        """
        self.assertEqual(get_index_from_number(1), (0, 0))

    def test_9_is_zero_in_mas(self):
        """
        Тест на наличие в массиве пустых клеток.
        """
        mas = [
            [2, 2, 2, 2],
            [2, 4, 2, 4],
            [4, 2, 4, 2],
            [4, 4, 4, 4]
        ]
        self.assertEqual(is_zero_in_mas(mas), False)

    def test_10_is_zero_in_mas(self):
        """
        Тест на наличие в массиве пустых клеток.
        """
        mas = [
            [2, 2, 2, 2],
            [2, 0, 2, 4],
            [4, 2, 4, 2],
            [4, 4, 4, 4]
        ]
        self.assertEqual(is_zero_in_mas(mas), True)

    def test_11_is_zero_in_mas(self):
        """
        Тест на наличие в массиве пустых клеток.
        """
        mas = [
            [0, 2, 2, 2],
            [2, 4, 0, 4],
            [4, 0, 4, 2],
            [4, 4, 0, 4]
        ]
        self.assertEqual(is_zero_in_mas(mas), True)

    def test_12_move_left(self):
        """
        Тест на движение клеток влево.
        """
        mas = [
            [2, 2, 0, 0],
            [0, 4, 4, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        rezult = [
            [4, 0, 0, 0],
            [8, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(move_left(mas), (rezult, 12))

    def test_13_move_left(self):
        """
        Тест на движение клеток влево.
        """
        mas = [
            [2, 4, 4, 2],
            [4, 0, 0, 2],
            [0, 0, 0, 0],
            [8, 8, 4, 4]
        ]
        rezult = [
            [2, 8, 2, 0],
            [4, 2, 0, 0],
            [0, 0, 0, 0],
            [16, 8, 0, 0]
        ]
        self.assertEqual(move_left(mas), (rezult, 32))

    def test_14_move_right(self):
        """
        Тест на движение клеток влево.
        """
        mas = [
            [2, 2, 0, 0],
            [0, 4, 4, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        rezult = [
            [0, 0, 0, 4],
            [0, 0, 0, 8],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(move_right(mas), (rezult, 12))

    def test_15_move_right(self):
        """
        Тест на движение клеток влево.
        """
        mas = [
            [2, 4, 4, 2],
            [4, 0, 0, 2],
            [0, 0, 0, 0],
            [8, 8, 4, 4]
        ]
        rezult = [
            [0, 2, 8, 2],
            [0, 0, 4, 2],
            [0, 0, 0, 0],
            [0, 0, 16, 8]
        ]
        self.assertEqual(move_right(mas), (rezult, 32))

    def test_16_move_up(self):
        """
        Тест на движение клеток вверх.
        """
        mas = [
            [2, 4, 0, 2],
            [2, 0, 2, 0],
            [4, 0, 2, 4],
            [4, 4, 0, 0]
        ]
        rezult = [
            [4, 8, 4, 2],
            [8, 0, 0, 4],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(move_up(mas), (rezult, 24))

    def test_17_move_down(self):
        """
        Тест на движение клеток вниз.
        """
        mas = [
            [2, 4, 0, 2],
            [2, 0, 2, 0],
            [4, 0, 2, 4],
            [4, 4, 0, 0]
        ]
        rezult = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [4, 0, 0, 2],
            [8, 8, 4, 4]
        ]
        self.assertEqual(move_down(mas), (rezult, 24))

    def test_18_can_move(self):
        """
        Тест на возможность сделать ход.
        """
        mas = [
            [2, 4, 0, 2],
            [2, 0, 2, 0],
            [4, 0, 2, 4],
            [4, 4, 0, 0]
        ]
        self.assertEqual(can_move(mas), True)

    def test_19_can_move(self):
        """
        Тест на возможность сделать ход.
        """
        mas = [
            [2, 4, 32, 2],
            [32, 8, 16, 8],
            [4, 2, 8, 4],
            [16, 32, 64, 32]
        ]
        self.assertEqual(can_move(mas), False)


if __name__ == "main":
    unittest.main
