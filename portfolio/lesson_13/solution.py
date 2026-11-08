"""Занятие 13. Строки: нормализация, частоты и кодировки.

Заполните тела функций. Проверка: python -m pytest tests.py -v
Замер: python bench.py
Правила нормализации записаны в документации каждой функции: тесты проверяют
эти правила, поэтому другие правила (например, замена ё на е) тесты не пройдут.
"""
import unicodedata
from collections import Counter


def normalize_name(text):
    """ФИО из формы в едином виде. Задача 0, нормализация ввода.

    1. Unicode NFC.
    2. Пробелы по краям убраны, серия пробельных символов заменена одним пробелом.
    3. В каждом слове первая буква заглавная, остальные строчные; части двойной фамилии через дефис оформляются так же: 'Салтыков-Щедрин'. Буква ё сохраняется,
    а пустая строка и строка из пробелов дают ''.
    Время O(n), память O(n).
    """
    s = unicodedata.normalize('NFC', text)
    s = ' '.join(s.split())
    parts = []
    for word in s.split(' '):
        pieces = word.split('-')
        word = '-'.join(p[:1].upper() + p[1:].lower() for p in pieces)
        parts.append(word)
    return ' '.join(parts)

def letters(text):
    """Значимые символы для сравнения: NFC, casefold, только буквы и цифры.

    Возвращает список символов. Пример: 'А роза!' --> ['а', 'р', 'о', 'з', 'а'].
    """
    s = unicodedata.normalize('NFC', text).casefold()
    return [c for c in s if c.isalnum()]


def is_anagram(a, b):
    """Анаграммы, LeetCode 242. Задача 1 занятия 13.

    Строки сравниваются после letters: регистр, пробелы и знаки не важны,
    ё и е - разные буквы. Обе строки без букв и цифр — анаграммы (True).
    Решение - частотный словарь. Время O(n + m), память O(k),
    где k - число разных символов.
    """
    return Counter(letters(a)) == Counter(letters(b))


def first_unique(text):
    """Первая буква, которая встречается один раз, LeetCode 387. Задача 2.

    Буквы сравниваются без учёта регистра: 'К' и 'к' - одна буква.
    Символы, которые не буквы (str.isalpha), не рассматриваются.
    Возвращает индекс в исходной строке или -1. Строка приходит в форме NFC.
    Время O(n), память O(k).
    """
    low = text.casefold()
    counts = Counter(c for c in low if c.isalpha())
    for i, ch in enumerate(text):
        if ch.isalpha() and counts[ch.casefold()] == 1:
            return i
    return -1


def can_construct(note, magazine):
    """Записка из букв журнала, LeetCode 383. Задача 3, расширение.

    Можно ли составить note из символов magazine, если каждый символ
    журнала используется не больше одного раза. Символы сравниваются как есть,
    с регистром и пробелами. Пустую записку можно составить всегда.
    Время O(n + m), память O(k).
    """
    if len(note) > len(magazine):
        return False
    return not (Counter(note) - Counter(magazine))

def find_anagrams(s, p):
    """Индексы начала всех подстрок s, являющихся анаграммами p.

    LeetCode 438. Символы сравниваются как есть (регистр и знаки значимы).
    Время O(n · k), k — число разных символов в p. Окно не пересчитываем.
    """
    n, m = len(s), len(p)
    if m == 0 or m > n:
        return []
    need = Counter(p)
    window = Counter(s[:m])
    res = []
    if window == need:
        res.append(0)
    for i in range(m, n):
        right, left = s[i], s[i - m]
        window[right] += 1
        window[left] -= 1
        if window[left] == 0:
            del window[left]
        if window == need:
            res.append(i - m + 1)
    return res