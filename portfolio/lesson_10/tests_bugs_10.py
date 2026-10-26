"""Тесты к bugs_10.py. Запуск: python -m pytest tests_bugs_10.py -v

Каждый тест должен падать на исходной версии функции и проходить после исправления.
"""
import pytest
from bugs_10 import max_ones, longest_k_distinct, shortest_at_least

def test_max_ones_boundary():
    # При k=0 и элементе 0 старый код выдавал 1 вместо 0
    assert max_ones([0], 0) == 0

def test_longest_k_distinct_boundary():
    # Для пустой строки старый код выдавал 1 вместо 0
    assert longest_k_distinct("", 2) == 0

def test_shortest_at_least_boundary():
    # При s=0 старый код уходил в бесконечный цикл/IndexError из-за total >= 0
    with pytest.raises(ValueError):
        shortest_at_least([1, 2, 3], 0)