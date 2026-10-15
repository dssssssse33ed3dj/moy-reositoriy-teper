"""Тесты домашнего задания № 5. Запуск из корня репозитория:

    pytest lesson_05 -q
"""

import random
import threading

import pytest

from solution_05 import decrypt, step_score


def finishes_within(seconds, func, *args):
    """Запускает func(*args) в отдельном потоке и ждёт не дольше seconds.

    Медленное решение не вешает pytest: тест падает по истечении лимита,
    а недосчитавший поток закрывается вместе с pytest.
    """
    done = threading.Event()
    errors = []

    def work():
        try:
            func(*args)
        except Exception as error:  # ошибку решения показываем как есть
            errors.append(error)
        done.set()

    threading.Thread(target=work, daemon=True).start()
    finished = done.wait(seconds)
    if errors:
        raise errors[0]
    return finished


# ---------- Задача 1. Очки фитнес-браслета ----------

def score_brute(steps, k, lower, upper):
    score = 0
    for s in range(len(steps) - k + 1):
        total = sum(steps[s:s + k])
        if total < lower:
            score -= 1
        elif total > upper:
            score += 1
    return score


@pytest.mark.parametrize("steps, k, lower, upper, expected", [
    ([1, 2, 3, 4, 5], 1, 3, 3, 0),
    ([3, 2], 2, 0, 1, 1),
    ([6, 5, 0, 0], 2, 1, 5, 0),
], ids=["example_1", "example_2", "example_3"])
def test_score_examples(steps, k, lower, upper, expected):
    assert step_score(steps, k, lower, upper) == expected


def test_score_k_is_one():
    assert step_score([2, 9, 5], 1, 3, 6) == 0      # −1, +1, 0


def test_score_k_is_n():
    assert step_score([6000, 5000, 7000], 3, 10_000, 15_000) == 1


def test_score_bounds_are_inclusive():
    # Сумма, равная lower или upper, — ноль очков, а не минус и не плюс.
    assert step_score([5, 5, 5], 2, 10, 20) == 0, "сумма ровно lower дала минус"
    assert step_score([10, 10, 10], 2, 0, 20) == 0, "сумма ровно upper дала плюс"


def test_score_all_low():
    assert step_score([1, 1, 1, 1, 1], 2, 10, 20) == -4


def test_score_does_not_change_input():
    steps = [7, 1, 4, 2]
    step_score(steps, 2, 3, 6)
    assert steps == [7, 1, 4, 2], "функция изменила список steps"


def test_score_matches_brute_force():
    rnd = random.Random(9)
    for _ in range(300):
        steps = [rnd.randint(0, 20) for _ in range(rnd.randint(1, 15))]
        k = rnd.randint(1, len(steps))
        lower = rnd.randint(0, 10 * k)
        upper = rnd.randint(lower, 20 * k)
        assert step_score(steps, k, lower, upper) == score_brute(steps, k, lower, upper)


def test_score_fast_enough():
    rnd = random.Random(90)
    steps = [rnd.randint(0, 20_000) for _ in range(200_000)]
    assert finishes_within(2, step_score, steps, 100_000, 900_000_000, 1_100_000_000), \
        "окно длины 100 000 дольше 2 секунд: сумма окна пересчитывается заново"


# ---------- Задача 2. Кодовый замок ----------

def decrypt_brute(code, k):
    n = len(code)
    if k > 0:
        return [sum(code[(i + j) % n] for j in range(1, k + 1)) for i in range(n)]
    if k < 0:
        return [sum(code[(i - j) % n] for j in range(1, -k + 1)) for i in range(n)]
    return [0] * n


@pytest.mark.parametrize("code, k, expected", [
    ([5, 7, 1, 4], 3, [12, 10, 16, 13]),
    ([1, 2, 3, 4], 0, [0, 0, 0, 0]),
    ([2, 4, 9, 3], -2, [12, 5, 6, 13]),
], ids=["example_1", "example_2", "example_3"])
def test_decrypt_examples(code, k, expected):
    assert decrypt(code, k) == expected


def test_decrypt_one_number():
    assert decrypt([7], 0) == [0]


def test_decrypt_k_is_one():
    assert decrypt([1, 2, 3], 1) == [2, 3, 1]


def test_decrypt_k_is_minus_one():
    assert decrypt([1, 2, 3], -1) == [3, 1, 2]


def test_decrypt_widest_window():
    # |k| = n − 1: в сумму входят все числа, кроме своего.
    assert decrypt([1, 2, 3, 4], 3) == [9, 8, 7, 6]
    assert decrypt([1, 2, 3, 4], -3) == [9, 8, 7, 6]


def test_decrypt_returns_new_list():
    code = [5, 7, 1, 4]
    result = decrypt(code, 2)
    assert code == [5, 7, 1, 4], "функция изменила список code"
    assert result is not code


def test_decrypt_matches_brute_force():
    rnd = random.Random(10)
    for _ in range(300):
        code = [rnd.randint(1, 100) for _ in range(rnd.randint(1, 12))]
        k = rnd.randint(-(len(code) - 1), len(code) - 1)
        assert decrypt(code, k) == decrypt_brute(code, k), (code, k)


def test_decrypt_fast_enough():
    rnd = random.Random(100)
    code = [rnd.randint(1, 100) for _ in range(200_000)]
    assert finishes_within(2, decrypt, code, 100_000), \
        "200 000 чисел при k = 100 000 дольше 2 секунд: сумма окна пересчитывается заново"
    assert finishes_within(2, decrypt, code, -100_000), \
        "200 000 чисел при k = −100 000 дольше 2 секунд: сумма окна пересчитывается заново"
