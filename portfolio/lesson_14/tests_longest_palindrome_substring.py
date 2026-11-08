"""Тесты к longest_palindrome_substring. 
Запуск: python -m pytest tests_longest_palindrome_substring.py -v"""

import pytest
from solution import longest_palindrome_substring


def is_pal(t):
    return t == t[::-1]


@pytest.mark.parametrize("s, want_len", [
    ('babad', 3),  # 'bab' или 'aba'
    ('cbbd', 2),  # 'bb'
    ('', 0),      # пустая
    ('a', 1),   # один символ
    ('abba', 4),  # чётный палиндром - вся строка
    ('абабаб', 5),   # кириллица: 'абаба' или 'бабаб'
    ('абв', 1),   # без повторов
], ids=["babad", "cbbd", "empty", "one", "even", "cyrillic", "no_repeats"])
def test_longest_palindrome_substring(s, want_len):
    got = longest_palindrome_substring(s)

    assert len(got) == want_len, f'длина {len(got)} вместо {want_len}: {got!r}'
    assert is_pal(got), f'не палиндром: {got!r}'
    assert got in s, f'подстроки {got!r} нет в {s!r}'