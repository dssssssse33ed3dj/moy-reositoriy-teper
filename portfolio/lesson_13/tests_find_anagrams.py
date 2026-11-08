"""Тесты к find_anagrams Запуск: python -m pytest tests_find_anagrams.py -v"""
import pytest

from solution import find_anagrams


@pytest.mark.parametrize("s, p, want", [
    ('cbaebabacd', 'abc', [0, 6]),  # пример LC
    ('abab', 'ab', [0, 1, 2]),   # пример LC
    ('abc', 'abcd', []),    # p длиннее s
    ('ааааа', 'аа', [0, 1, 2, 3]), # повторы в p
    ('абабаб', 'аб', [0, 1, 2, 3, 4]),  # кириллица, перекрытия
    ('abc', 'xyz', []),   # вхождений нет
], ids=["lc1", "lc2_overlap", "p_longer", "repeats", "cyrillic", "none"])
def test_find_anagrams(s, p, want):
    assert find_anagrams(s, p) == want