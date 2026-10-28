"""Тесты к bugs_12.py. Запуск: python -m pytest tests_bugs_12.py -v

Каждый тест должен падать на исходной версии функции и проходить после исправления.
"""

from bugs_12 import busy_hours, first_conflict, longest_busy


def test_busy_hours_boundary():
    # Нарушено - reach уменьшался на вложенном интервале
    assert busy_hours([[1, 10], [2, 5]]) == 9


def test_first_conflict_boundary():
    # Нарушено - цикл не доходил до последней пары
    assert first_conflict([[1, 3], [4, 6], [5, 7]]) == [[4, 6], [5, 7]]


def test_longest_busy_boundary():
    # Нарушено - касающиеся интервалы не склеивались
    assert longest_busy([[1, 4], [4, 9]]) == 8