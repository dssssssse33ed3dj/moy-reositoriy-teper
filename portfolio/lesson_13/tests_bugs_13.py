"""Тесты к bugs_13.py. Запуск: python -m pytest tests_bugs_13.py -v

Каждый тест должен падать на функции из bugs_13.py как она есть
и проходить после исправления одной строки.
"""
from bugs_13 import all_unique, is_pangram_ru, top_letter


def test_is_pangram_ru_edge():
    # все 33 буквы, кроме ё — не панграмма
    text = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    assert is_pangram_ru(text) is False


def test_top_letter_edge():
    # у 'б' и 'а' частота 1, 'б' встретилась раньше — она и ответ
    assert top_letter('ба') == 'б'


def test_all_unique_edge():
    # 'А' и 'а' — одна буква, значит не all_unique
    assert all_unique('Аа') is False