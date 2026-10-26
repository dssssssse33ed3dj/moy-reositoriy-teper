"""Занятие 7 · массив: индексы, проходы, границы.

Три функции для самостоятельного решения. Сигнатуры и контракты не меняйте:
по ним работают тесты в tests.py. Условия и ограничения — в task.md.

Запуск тестов из этой папки:
    python -m pytest tests.py -v
"""


def max_streak(steps: list[int], goal: int = 10_000) -> int:
    """Длина самой длинной серии дней подряд, в которые шагов было не меньше goal.

    steps - число шагов по дням, в порядке дат. Пустой список → 0
    Время O(n), дополнительная память O(1). Список не изменяется

    """
    max_streak_len = 0
    current_streak = 0
    
    for day_steps in steps:
        if day_steps >= goal:
            current_streak += 1
            if current_streak > max_streak_len:
                max_streak_len = current_streak
        else:
            current_streak = 0
            
    return max_streak_len


def reverse_segment(tracks: list, l: int, r: int) -> None:
    """Разворачивает участок плейлиста tracks[l..r] включительно на месте

    Элементы вне участка остаются на своих местах. Функция ничего не возвращает
    Если не выполнено 0 <= l <= r < len(tracks), поднимается ValueError,
    а список остаётся без изменений.
    Время O(r-l), дополнительная память O(1). Срезы и reversed() не используются.
    """
    raise NotImplementedError


def is_spam(text: str) -> bool:
    """Комментарий считается спамом, если в нём есть ссылка."""
    return "http://" in text or "https://" in text


def remove_spam(comments: list[str]) -> int:
    """Удаляет спам из списка комментариев на месте и возвращает число оставшихся.

    Порядок обычных комментариев сохраняется. После вызова в списке остаются
    только обычные комментарии: len(comments) равна возвращённому числу.
    Время O(n), дополнительная память O(1): новый список не создаётся,
    remove(), del по одному элементу внутри цикла и генераторы списков не используются.


    """
    write_index = 0
    
    # Шаг 1: Сдвигаем все полезные комментарии в начало списка за один проход O(n)
    for read_index in range(len(comments)):
        if not is_spam(comments[read_index]):
            comments[write_index] = comments[read_index]
            write_index += 1
            
    # Шаг 2: Обрезаем хвост списка до реального количества оставшихся элементов
    # Суммарное время работы функции строго O(n), доп. память O(1).
    while len(comments) > write_index:
        comments.pop()
        
    return write_index
