"""Занятие 12. Интервалы: сортировка как инструмент решения.

Интервал записан списком [start, end] и означает полуинтервал [start, end):
момент start входит в интервал, момент end — нет. Везде start < end.
Заполните тела функций. Проверка: python -m pytest tests.py -v
Замер: python bench.py
"""


def overlaps(a, b):
    """Пересекаются ли два интервала. Задача 0, разминка.

    a и b — интервалы [start, end). Интервалы, которые только касаются
    (конец одного равен началу другого), не пересекаются. Время O(1).
    """
    return max(a[0], b[0]) < min(a[1], b[1])


def merge_intervals(intervals):
    """Объединение пересекающихся интервалов, LeetCode 56. Задача 1 занятия 12.

    intervals — список интервалов в любом порядке, может быть пустым.
    Пересекающиеся и касающиеся интервалы склеиваются в один блок.
    Возвращает новый список блоков по возрастанию начала. Список intervals
    и интервалы в нём не меняются. Время O(n log n), память O(n).
    """
    if not intervals:
        return []
    
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    merged = [list(sorted_intervals[0])]
    
    for current in sorted_intervals[1:]:
        prev = merged[-1]
        if prev[1] >= current[0]:
            prev[1] = max(prev[1], current[1])
        else:
            merged.append(list(current))
            
    return merged


def can_attend(intervals):
    """Встречи без конфликтов, LeetCode 252. Задача 2 занятия 12.

    intervals — встречи [start, end) в любом порядке, может быть пустым.
    Возвращает True, если никакие две встречи не пересекаются: тогда все
    можно провести в одной переговорной. Касание конфликтом не считается.
    Список intervals не меняется. Время O(n log n), память O(n).
    """
    if not intervals:
        return True
        
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    
    for i in range(len(sorted_intervals) - 1):
        if sorted_intervals[i][1] > sorted_intervals[i + 1][0]:
            return False
            
    return True


def insert_interval(intervals, new):
    """Вставка интервала, LeetCode 57. Задача 3, расширение.

    intervals — blocks по возрастанию начала, без пересечений и касаний
    (такой список возвращает merge_intervals). new — интервал [start, end).
    Возвращает новый список блоков, в который добавлен new; пересекающиеся
    и касающиеся блоки склеены. Сортировать не нужно: время O(n).
    """
    res = []
    i = 0
    n = len(intervals)
    new_start, new_end = new
    
    while i < n and intervals[i][1] < new_start:
        res.append(list(intervals[i]))
        i += 1
        
    while i < n and intervals[i][0] <= new_end:
        new_start = min(new_start, intervals[i][0])
        new_end = max(new_end, intervals[i][1])
        i += 1
    res.append([new_start, new_end])
    
    while i < n:
        res.append(list(intervals[i]))
        i += 1
        
    return res


def count_free_days(days: int, meetings: list[list[int]]) -> int:
    """Возвращает количество дней без встреч (границы [start, end] включительно)."""
    if not meetings:
        return days
        
    sorted_meetings = sorted(meetings, key=lambda x: x[0])
    merged = []
    curr_start, curr_end = sorted_meetings[0]
    
    for next_start, next_end in sorted_meetings[1:]:
        if curr_end + 1 >= next_start:
            curr_end = max(curr_end, next_end)
        else:
            merged.append((curr_start, curr_end))
            curr_start, curr_end = next_start, next_end
    merged.append((curr_start, curr_end))
    
    busy_days = 0
    for start, end in merged:
        act_start = max(1, start)
        act_end = min(days, end)
        if act_start <= act_end:
            busy_days += (act_end - act_start + 1)
            
    return max(0, days - busy_days)