"""Тесты к bugs_11.py. Запуск: python -m pytest tests_bugs_11.py -v

Каждый тест должен падать на исходной версии функции и проходить после исправления.
"""

import pytest
from bugs_11 import longest_zero_sum, last_pivot_index, max_query_sum

def test_longest_zero_sum_boundary():
    # Старый код на [1, -1] выдавал 0 вместо 2, так как не знал префикс 0 на старте
    assert longest_zero_sum([1, -1]) == 2

def test_last_pivot_index_boundary():
    # Старый код на [0, 0, 0] не доходил до индекса 0 и возвращал -1 вместо 0 (или самого правого баланса, если 0 подходит)
    # На [1, 2, 3] равновесного индекса нет вовсе, а на [2, 0, 0] самый правый баланс — это индекс 0 (слева 0, справа 0)
    assert last_pivot_index([2, 0, 0]) == 0

def test_max_query_sum_boundary():
    # Старый код на чисто отрицательных числах выдавал 0 вместо -1, так как best инициализировался нулем
    assert max_query_sum([-5, -1, -3], [(1, 2)]) == -1