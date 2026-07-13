import unittest
from main import get_number_from_index, get_empty_list, get_index_from_number


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


if __name__ == "main":
    unittest.main
