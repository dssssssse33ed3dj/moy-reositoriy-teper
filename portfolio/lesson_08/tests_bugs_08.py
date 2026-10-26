"""Тесты к bugs_08.py. Запуск: python -m pytest tests_bugs_08.py -v

Каждый тест должен падать на исходной версии функции и проходить после исправления.
"""

from bugs_08 import count_cheap_pairs, dedup_keep_two, is_mirror


def test_count_cheap_pairs_boundary():
    # Баг 1: считает сумму равную limit как строго меньшую limit
    # prices =, limit = 4. 1 + 3 = 4 (не строго меньше). Ответ должен быть 0
    assert count_cheap_pairs([1, 3], 4) == 0


def test_dedup_keep_two_boundary():
    # Баг 2: для коротких списков (меньше 2 элементов) возвращает длину 2 и портит структуру
    # Для списка 5 ответ должен быть 1, а список должен остаться 5
    ids = [5]
    assert dedup_keep_two(ids) == 1
    assert ids == [5]


def test_is_mirror_boundary():
    # Баг 3: для двух разных элементов не заходит в цикл и возвращает True вместо False
    assert is_mirror(["a", "b"]) is False