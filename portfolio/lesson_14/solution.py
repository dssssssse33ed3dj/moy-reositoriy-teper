"""Занятие 14. Палиндромы и симметричные проверки.

Заполните тела функций. Проверка: python -m pytest tests.py -v
Замер: python bench.py
"""
from collections import Counter


def is_palindrome(text):
    """Палиндром с пропуском символов, LeetCode 125. Задача 1 занятия 14.

    Сравниваются только буквы и цифры (str.isalnum) без учёта регистра
    (casefold); ё и е — разные буквы. Строка приходит в форме NFC.
    Строка без букв и цифр — палиндром (True).
    Два указателя навстречу, без копии строки: время O(n), память O(1).
    """
    i, j = 0, len(text) - 1
    while i < j:
        while i < j and not text[i].isalnum():
            i += 1
        while i < j and not text[j].isalnum():
            j -= 1
        if text[i].casefold() != text[j].casefold():
            return False
        i += 1
        j -= 1
    return True


def is_palindrome_copy(text):
    """То же, что is_palindrome, через очищенную копию и её разворот.

    Нужна для сравнения в замере: время O(n), память O(n).
    """
    cleaned = [ch.casefold() for ch in text if ch.isalnum()]
    return cleaned == cleaned[::-1]


def can_be_palindrome(s):
    """Палиндром после удаления не более одного символа, LeetCode 680. Задача 2.

    Символы сравниваются как есть, без нормализации. Время O(n), память O(1).
    Пример: 'abca' → True (удалить 'b' или 'c'), 'abc' → False.
    """
    def is_pal(lo, hi):
        while lo < hi:
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True

    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return is_pal(i + 1, j) or is_pal(i, j - 1)
        i += 1
        j -= 1
    return True


def removal_index(s):
    """Восстановление ответа к задаче 2: какой символ удалить.

    -1 — строка уже палиндром, удалять ничего не нужно.
    k — индекс символа, после удаления которого s становится палиндромом;
        если подходят несколько индексов, вернуть любой из них.
    None — одного удаления не хватает.
    Время O(n), память O(1).
    """
    def is_pal(lo, hi):
        while lo < hi:
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True

    if is_pal(0, len(s) - 1):
        return -1
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            if is_pal(i + 1, j):
                return i
            if is_pal(i, j - 1):
                return j
            return None
        i += 1
        j -= 1
    return -1


def longest_palindrome_length(s):
    """Длина самого длинного палиндрома из букв s, LeetCode 409. Задача 3, расширение.

    Буквы можно переставлять, каждая используется не больше одного раза.
    Регистр важен: 'A' и 'a' — разные буквы. Время O(n), память O(k).
    Пример: 'abccccdd' → 7 (например, 'dccaccd').
    """
    counts = Counter(s)
    total = sum(c // 2 * 2 for c in counts.values())
    if any(c % 2 == 1 for c in counts.values()):
        total += 1
    return total

def longest_palindrome_substring(s):
    """Самая длинная подстрока s, являющаяся палиндромом. LeetCode 5.

    Символы сравниваются как есть. Если ответов несколько — любой.
    O(n²) время, O(1) память: расширяемся из каждого центра, без таблицы n × n.
    """
    if not s:
        return ''
    best_l, best_r = 0, 0

    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return l + 1, r - 1

    for i in range(len(s)):
        l1, r1 = expand(i, i)          # нечётный центр
        if r1 - l1 > best_r - best_l:
            best_l, best_r = l1, r1
        l2, r2 = expand(i, i + 1)      # чётный центр
        if r2 - l2 > best_r - best_l:
            best_l, best_r = l2, r2
    return s[best_l:best_r + 1]