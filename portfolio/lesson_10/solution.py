"""Занятие 10. Скользящее окно переменного размера.

Заполните тела функций. Проверка: python -m pytest tests.py -v
Замер: python bench.py
"""


def longest_within(nums, limit):
    """Самый длинный отрезок с суммой не больше limit. Задача 0, схема прохода.

    nums — список целых неотрицательных чисел, может быть пустым.
    limit — лимит суммы, limit >= 0; иначе ValueError.
    Возвращает длину самого длинного отрезка подряд с суммой не больше limit.
    Если такого отрезка нет, возвращает 0. Список не меняется.
    Время O(n), память O(1).
    """
    if limit < 0:
        raise ValueError("Limit cannot be negative")
    
    max_len = 0
    current_sum = 0
    left = 0
    
    for right in range(len(nums)):
        current_sum += nums[right]
        
        while current_sum > limit and left <= right:
            current_sum -= nums[left]
            left += 1
            
        max_len = max(max_len, right - left + 1)
        
    return max_len


def shortest_window(nums, s):
    """Окно переменного размера. Задача 1 занятия 10.

    nums — список целых неотрицательных чисел, может быть пустым.
    s — порог суммы, s >= 1; иначе ValueError.
    Возвращает длину самого короткого отрезка подряд с суммой не меньше s.
    Если такого отрезка нет, возвращает 0. Список не меняется.
    Время O(n), память O(1).
    """
    if s < 1:
        raise ValueError("s must be at least 1")
        
    min_len = float('inf')
    current_sum = 0
    left = 0
    
    for right in range(len(nums)):
        current_sum += nums[right]
        
        while current_sum >= s:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1
            
    return min_len if min_len != float('inf') else 0


def longest_unique(text):
    """Окно переменного размера с частотной картой. Задача 2 занятия 10.

    text — строка из любых символов, может быть пустой.
    Возвращает длину самой длинной подстроки, в которой все символы разные.
    Регистр различается: 'a' и 'A' — разные символы. Для пустой строки — 0.
    Время O(n), память O(m), m — число разных символов строки.
    """
    max_len = 0
    char_index = {}
    left = 0
    
    for right in range(len(text)):
        char = text[right]
        
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
            
        char_index[char] = right
        max_len = max(max_len, right - left + 1)
        
    return max_len


def total_fruit(fruits):
    """Две корзины, LeetCode 904. Задача 3, расширение.

    fruits — список целых чисел, fruits[i] — вид фрукта на пределе i; может быть пустым.
    Возвращает длину самого длинного отрезка подряд, в котором не больше двух разных чисел.
    Список не меняется. Время O(n), память O(1).
    """
    max_fruits = 0
    basket = {}
    left = 0
    
    for right in range(len(fruits)):
        fruit = fruits[right]
        basket[fruit] = basket.get(fruit, 0) + 1
        
        while len(basket) > 2:
            left_fruit = fruits[left]
            basket[left_fruit] -= 1
            if basket[left_fruit] == 0:
                del basket[left_fruit]
            left += 1
            
        max_fruits = max(max_fruits, right - left + 1)
        
    return max_fruits