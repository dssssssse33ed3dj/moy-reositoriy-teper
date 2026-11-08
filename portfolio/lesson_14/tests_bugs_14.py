"""Тесты к bugs_14.py. Запуск: python -m pytest tests_bugs_14.py -v

Каждый тест должен падать на функции из bugs_14.py как она есть
и проходить после исправления одной строки.
"""
from bugs_14 import count_mismatches, is_word_palindrome, reverse_letters


def test_is_word_palindrome_edge():
    # два пробела подряд. лишняя пустая строка ломает сравнение
    assert is_word_palindrome('кот  ест кот') is True


def test_reverse_letters_edge():
    # строка без букв: i убегает за границу → IndexError
    assert reverse_letters('123') == '123'


def test_count_mismatches_edge():
    # чётная длина: центральная пара считается дважды
    assert count_mismatches('аб') == 1