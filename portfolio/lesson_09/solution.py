"""Занятие 9. Скользящее окно фиксированного размера.

Заполните тела функций. Проверка: python -m pytest tests.py -v
Замер: python bench.py
"""


def window_sums_slices(nums, k):
    """Сумма каждого окна срезами. Задача 0, первая версия.

    nums — список целых чисел, k — длина окна, 1 <= k <= len(nums), иначе ValueError.
    Возвращает новый список из len(nums) - k + 1 сумм: на месте s — sum(nums[s:s + k]).
    Список nums не меняется. Время O(n·k).
    """
    if not isinstance(k, int) or not (1 <= k <= len(nums)):
        raise ValueError("Неверный размер окна k")
    
    result = []
    for i in range(len(nums) - k + 1):
        result.append(sum(nums[i:i + k]))
    return result


def window_sums(nums, k):
    """Сумма каждого окна сдвигом. Задача 0, вторая версия.

    Тот же контракт, что у window_sums_slices.
    Первое окно складывается целиком, дальше: плюс пришедший, минус ушедший элемент.
    Время O(n), память O(1) кроме ответа.
    """
    if not isinstance(k, int) or not (1 <= k <= len(nums)):
        raise ValueError("Неверный размер окна k")
    
    current_sum = 0
    for i in range(k):
        current_sum += nums[i]
        
    result = [current_sum]
    for i in range(k, len(nums)):
        current_sum = current_sum - nums[i - k] + nums[i]
        result.append(current_sum)
    return result


def best_window(nums, k):
    """Лучший отрезок длины k. Задача 1 занятия 9.

    nums — список целых чисел, числа могут быть отрицательными.
    k — длина окна, 1 <= k <= len(nums); иначе ValueError.
    Возвращает (start, total): начало окна длины k с наибольшей суммой и эту сумму.
    При равных суммах — самое левое окно. Список не меняется.
    Время O(n), память O(1).
    """
    if not isinstance(k, int) or not (1 <= k <= len(nums)):
        raise ValueError("Неверный размер окна k")
    
    current_sum = 0
    for i in range(k):
        current_sum += nums[i]
        
    best_start = 0
    max_sum = current_sum
    
    for i in range(k, len(nums)):
        current_sum = current_sum - nums[i - k] + nums[i]
        if current_sum > max_sum:
            max_sum = current_sum
            best_start = i - k + 1
            
    return best_start, max_sum


def max_events(times, w):
    """События во временном окне. Задача 2 занятия 9.

    times — моменты событий по возрастанию, одинаковые моменты — разные события.
    w — длина окна в секундах, w > 0; иначе ValueError.
    Окно — полуинтервал [s, s + w). Возвращает наибольшее число событий в одном окне,
    для пустого списка — 0. Список не меняется. Время O(n), память O(1).
    """
    if w <= 0:
        raise ValueError("Ширина окна должна быть больше нуля")
    if not times:
        return 0
        
    max_count = 0
    left = 0
    
    for right in range(len(times)):
        while times[right] - times[left] >= w:
            left += 1
        current_count = right - left + 1
        if current_count > max_count:
            max_count = current_count
            
    return max_count


def max_vowels(s, k):
    """Расширение. LeetCode 1456: наибольшее число гласных в подстроке длины k.

    s — строка из строчных латинских букв, 1 <= k <= len(s) по условию LeetCode.
    Гласные — a, e, i, o, u. Время O(n), память O(1).
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    current_vowels = 0
    for i in range(k):
        if s[i] in vowels:
            current_vowels += 1
            
    max_vowels_count = current_vowels
    
    for i in range(k, len(s)):
        if s[i - k] in vowels:
            current_vowels -= 1
        if s[i] in vowels:
            current_vowels += 1
        if current_vowels > max_vowels_count:
            max_vowels_count = current_vowels
            
    return max_vowels_count


def count_good_windows(arr, k, threshold):
    """Сколько окон длины k имеют среднее значение не меньше threshold.
    
    LeetCode 1343. Время O(n), память O(1).
    """
    if not isinstance(k, int) or not (1 <= k <= len(arr)):
        raise ValueError("Неверный размер окна k")
        
    target_sum = threshold * k
    current_sum = sum(arr[:k])
    count = 1 if current_sum >= target_sum else 0
    
    for i in range(k, len(arr)):
        current_sum = current_sum - arr[i - k] + arr[i]
        if current_sum >= target_sum:
            count += 1
            
    return count