"""Тесты к bugs_09.py. Запуск: python -m pytest tests_bugs_09.py -v

Каждый тест должен падать на исходной версии функции и проходить после исправления.
"""
import pytest
from bugs_09 import count_in_window, count_strong_windows, min_window


def test_count_strong_windows_boundary():
    # Падал, потому что при k == len(nums) функция ошибочно кидала ValueError
    assert count_strong_windows([1, 2, 3], 3, 5) == 1


def test_min_window_boundary():
    # Падал, потому что при равных суммах (4 и 4) функция выдавала правое окно (индекс 1) вместо левого (0)
    assert min_window([1, 3, 1], 2) == (0, 4)


def test_count_in_window_boundary():
    # Падал, потому что функция считала элемент на правой границе (t == s + w), хотя окно полуоткрытое [s, s + w)
    assert count_in_window([5], 2, 3) == 0
