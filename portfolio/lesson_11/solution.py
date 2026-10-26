"""Занятие 11. Префиксные суммы и запросы на диапазоне.

Заполните тела функций. Проверка: python -m pytest tests.py -v
Замер: python bench.py
"""


def highest_altitude(gain):
    """Наибольшая высота на маршруте, LeetCode 1732. Задача 0, разминка.

    gain — список целых чисел: gain[i] — изменение высоты между точками i и i + 1.
    Маршрут начинается на высоте 0. Вернуть наибольшую высоту среди всех точек,
    включая начальную. Для пустого списка — 0. Время O(n), память O(1).
    """
    max_alt = 0
    current_alt = 0
    for g in gain:
        current_alt += g
        if current_alt > max_alt:
            max_alt = current_alt
    return max_alt


def range_sums(nums, queries):
    """Сервис сумм на диапазонах. Задача 1 занятия 11.

    nums — список целых чисел любого знака, может быть пустым.
    queries — список пар (l, r). Запрос — полуинтервал: сумма nums[l:r].
    Нужно 0 <= l <= r <= len(nums), иначе ValueError; при l == r сумма 0.
    Возвращает список ответов в порядке запросов. Список nums не меняется.
    Время O(n + q), память O(n).
    """
    n = len(nums)
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + nums[i]
        
    result = []
    for l, r in queries:
        if not (0 <= l <= r <= n):
            raise ValueError("Query indices out of bounds")
        result.append(pref[r] - pref[l])
        
    return result


def pivot_index(nums):
    """Равновесный индекс, LeetCode 724. Задача 2 занятия 11.

    nums — список целых чисел любого знака, может быть пустым.
    Возвращает самый левый индекс i, для которого сумма nums[:i] равна сумме nums[i + 1:].
    Если такого индекса нет, возвращает -1. Время O(n), память O(1).
    """
    total_sum = sum(nums)
    left_sum = 0
    for i, num in enumerate(nums):
        if left_sum == (total_sum - left_sum - num):
            return i
        left_sum += num
    return -1


def count_k_sums(nums, k):
    """Отрезки с суммой k, LeetCode 560. Задача 3, расширение.

    nums — список целых чисел любого знака, может быть пустым; k — любое целое.
    Возвращает число непустых отрезков подряд с суммой ровно k.
    Время O(n), память O(n).
    """
    count = 0
    current_sum = 0
    prefix_counts = {0: 1}
    
    for num in nums:
        current_sum += num
        if (current_sum - k) in prefix_counts:
            count += prefix_counts[current_sum - k]
        prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1
        
    return count


def count_vowel_ranges(words, queries):
    """Слова на гласную в диапазонах, LeetCode 2559.

    words — список строк (слов).
    queries — список пар [l, r], где l и r — включительные границы.
    Возвращает список ответов на запросы. Время O(n + q), память O(n).
    """
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 'у', 'е', 'а', 'о', 'э', 'я', 'и', 'ю', 'ы', 'ё'}
    n = len(words)
    
    # Строим массив префиксов. prefix[i] — количество подходящих слов среди первых i элементов
    prefix = [0] * (n + 1)
    for i in range(n):
        word = words[i]
        is_valid = 0
        if word and word[0] in vowels and word[-1] in vowels:
            is_valid = 1
        prefix[i + 1] = prefix[i] + is_valid
        
    result = []
    for l, r in queries:
        if not (0 <= l <= r < n):
            raise ValueError("Query indices out of bounds")
        # Так как r включительно, берем prefix[r + 1] вместо prefix[r]
        result.append(prefix[r + 1] - prefix[l])
        
    return result