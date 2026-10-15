"""Домашнее задание № 5. Скользящее окно фиксированного размера.

Заполните тела функций. Проверка из корня репозитория:

    pytest lesson_05 -q

    или python -m pytest -q

В обеих задачах нет срезов и вызовов sum внутри цикла: окно пересчитывается
сдвигом — плюс пришедший элемент, минус ушедший.
"""


def step_score(steps, k, lower, upper):
    """Задача 1. Очки фитнес-браслета (LeetCode 1176).

    steps[i] — число шагов в день i. Браслет оценивает каждые k дней подряд:
    сумма шагов меньше lower — минус одно очко, больше upper — плюс одно очко,
    от lower до upper включительно — ноль. Вернуть сумму очков по всем окнам.

    1 <= k <= len(steps), lower <= upper.
    Список steps не меняется. Время O(n).
    Пример: step_score([6, 5, 0, 0], 2, 1, 5) == 0.
    """
   
    if not steps or k <= 0:
        return 0

    # Считаем сумму самого первого окна размером k
    current_sum = sum(steps[:k])
    
    score = 0
    if current_sum < lower:
        score -= 1
    elif current_sum > upper:
        score += 1

    # Двигаем окно по всему списку за O(1) на каждый шаг
    for i in range(k, len(steps)):
        current_sum += steps[i] - steps[i - k]
        if current_sum < lower:
            score -= 1
        elif current_sum > upper:
            score += 1

    return score



def decrypt(code, k):
    """Задача 2. Кодовый замок (LeetCode 1652).

    code — числа, записанные по кругу: после последнего снова идёт первый.
    Каждое число заменяется одновременно:
      k > 0 — суммой k следующих чисел;
      k < 0 — суммой |k| предыдущих чисел;
      k == 0 — нулём.
    Вернуть новый список, code не меняется.

    В code хотя бы одно число, |k| < len(code).
    Время O(n), память O(1) кроме ответа.
    Пример: decrypt([5, 7, 1, 4], 3) == [12, 10, 16, 13].
    """
    n = len(code)
    result = [0] * n
    
    if k == 0:
        return result

    if k > 0:
        left = 1
        right = k
    else:
        left = n + k
        right = n - 1

    current_sum = 0
    idx = left
    for _ in range(abs(k)):
        current_sum += code[idx % n]
        idx += 1

    for i in range(n):
        result[i] = current_sum
     
        current_sum -= code[left % n]
        current_sum += code[(right + 1) % n]
        
        left += 1
        right += 1

    return result
