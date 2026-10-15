"""Домашнее задание № 4. Две задачи на изученные приёмы.

Заполните тела функций. Проверка из корня репозитория:

    pytest lesson_04 -q

    или python -m pytest -q

Какой из изученных приёмов подходит, решаете сами и отмечаете в homework_04.md.
"""


def min_boats(weights, limit):
    """Задача 1. Лодки на сплаве (LeetCode 881).

    weights — веса участников в килограммах, limit — грузоподъёмность одной лодки.
    В лодку садятся один или два человека, и их общий вес не больше limit.
    Вернуть наименьшее число лодок, чтобы переправить всех.

    Каждый вес от 1 до limit. Пустой список — 0 лодок.
    Список weights не меняется. Время O(n log n).
    Пример: min_boats([3, 5, 3, 4], 5) == 4.
    """
      
    if not weights:
        return 0
        
    sorted_weights = sorted(weights)
    
    left = 0
    right = len(sorted_weights) - 1
    boats = 0
    
    while left <= right:
        if left == right:
            boats += 1
            break
            
        if sorted_weights[left] + sorted_weights[right] <= limit:
            left += 1  
            
        right -= 1
        boats += 1
        
    return boats

def even_first(nums):
    """Задача 2. Сначала чётные (LeetCode 905).

    Переставить элементы списка nums на месте так, чтобы все чётные числа
    стояли раньше всех нечётных. Порядок внутри групп любой.
    Функция ничего не возвращает: меняется сам переданный список.
    Новые списки не создаются, дополнительная память O(1).
    Пример: [3, 1, 2, 4] → например, [2, 4, 3, 1] или [4, 2, 1, 3].
    """
    left = 0
    right = len(nums) - 1
    
    while left < right:
        # Если слева уже чётное, просто идём дальше
        if nums[left] % 2 == 0:
            left += 1
        # Если справа уже нечётное, просто сужаем границы
        elif nums[right] % 2 != 0:
            right -= 1
        # Если слева нечётное, а справа чётное — меняем их местами
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
