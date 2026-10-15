"""Тесты домашнего задания № 4. Запуск из корня репозитория:

    pytest lesson_04 -q
"""

import random
import threading
import tracemalloc

import pytest

from solution_04 import even_first, min_boats


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


# ---------- Задача 1. Лодки на сплаве ----------

def boats_brute(weights, limit):
    """Перебор всех способов рассадить: годится только для маленьких списков."""
    if not weights:
        return 0
    first, rest = weights[0], weights[1:]
    best = 1 + boats_brute(rest, limit)
    for i, w in enumerate(rest):
        if first + w <= limit:
            best = min(best, 1 + boats_brute(rest[:i] + rest[i + 1:], limit))
    return best


@pytest.mark.parametrize("weights, limit, expected", [
    ([1, 2], 3, 1),
    ([3, 2, 2, 1], 3, 3),
    ([3, 5, 3, 4], 5, 4),
], ids=["example_1", "example_2", "example_3"])
def test_boats_examples(weights, limit, expected):
    assert min_boats(weights, limit) == expected


def test_boats_empty():
    assert min_boats([], 100) == 0


def test_boats_one_person():
    assert min_boats([70], 100) == 1


def test_boats_all_fit_in_pairs():
    assert min_boats([50, 50, 50, 50], 100) == 2


def test_boats_nobody_fits_together():
    assert min_boats([60, 70, 80], 100) == 3


def test_boats_heavy_takes_lightest():
    # Самый тяжёлый (90) едет с самым лёгким (10), а не с соседом по весу.
    assert min_boats([10, 45, 55, 90], 100) == 2


def test_boats_does_not_change_input():
    weights = [80, 20, 50, 40]
    min_boats(weights, 100)
    assert weights == [80, 20, 50, 40], "функция изменила список weights"


def test_boats_matches_brute_force():
    rnd = random.Random(4)
    for _ in range(300):
        limit = rnd.randint(5, 30)
        weights = [rnd.randint(1, limit) for _ in range(rnd.randint(0, 8))]
        assert min_boats(weights, limit) == boats_brute(weights, limit), weights


def test_boats_fast_enough():
    rnd = random.Random(40)
    weights = [rnd.randint(1, 10_000) for _ in range(400_000)]
    assert finishes_within(2, min_boats, weights, 10_000), \
        "400 000 человек дольше 2 секунд: решение медленнее O(n log n)"


# ---------- Задача 2. Сначала чётные ----------

def check_even_first(before, after):
    assert sorted(after) == sorted(before), "состав списка изменился"
    parity = [x % 2 for x in after]
    assert parity == sorted(parity), f"нечётное число стоит раньше чётного: {after}"


@pytest.mark.parametrize("nums", [
    [3, 1, 2, 4],
    [0],
    [],
    [2, 4, 6],
    [1, 3, 5],
    [1, 2],
    [7, 8, 7, 8, 7, 8],
], ids=["example", "zero", "empty", "all_even", "all_odd", "odd_even", "alternating"])
def test_even_first(nums):
    before = list(nums)
    even_first(nums)
    check_even_first(before, nums)


def test_even_first_changes_same_list():
    nums = [1, 2, 3, 4]
    assert even_first(nums) is None, "функция меняет список на месте и ничего не возвращает"
    check_even_first([1, 2, 3, 4], nums)


def test_even_first_random():
    rnd = random.Random(5)
    for _ in range(300):
        nums = [rnd.randint(-50, 50) for _ in range(rnd.randint(0, 20))]
        before = list(nums)
        even_first(nums)
        check_even_first(before, nums)


def test_even_first_constant_memory():
    rnd = random.Random(51)
    nums = [rnd.randint(1, 10**6) for _ in range(100_000)]
    tracemalloc.start()
    even_first(nums)
    peak = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    assert peak < 50_000, f"занято {peak} байт: функция создаёт новые списки, а нужна память O(1)"


def test_even_first_fast_enough():
    rnd = random.Random(50)
    nums = [rnd.randint(1, 10**6) for _ in range(400_000)]
    assert finishes_within(2, even_first, nums), "400 000 чисел дольше 2 секунд: решение медленнее O(n)"
