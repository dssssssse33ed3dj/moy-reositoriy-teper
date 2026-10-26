"""Занятие 8. Два указателя.

Заполните тела функций. Проверка: python -m pytest tests.py -v
Замер: python bench.py
"""


def pair_sum_brute(prices, target):
    """Перебор всех пар. Задача 1, первая версия.

    prices — цены по возрастанию, target — сумма сертификата.
    Возвращает пару индексов (i, j), i < j, с prices[i] + prices[j] == target,
    или None, если такой пары нет. Список не меняется.
    Время O(n²), память O(1).
    """
    n = len(prices)
    for i in range(n):
        for j in range(i + 1, n):
            if prices[i] + prices[j] == target:
                return (i, j)
    return None


def pair_sum(prices, target):
    """Указатели навстречу. Задача 1, вторая версия.

    Тот же контракт, что у pair_sum_brute.
    Время O(n), память O(1).
    """
    left = 0
    right = len(prices) - 1
    
    while left < right:
        current_sum = prices[left] + prices[right]
        if current_sum == target:
            return (left, right)
        elif current_sum < target:
            left += 1
        else:
            right -= 1
            
    return None


def dedup_sorted(ids):
    """Удаление повторов из отсортированного списка на месте. Задача 2.

    После вызова в ids остаются различные значения по возрастанию.
    Возвращает их число. Новый список не создаётся, один del ids[k:] после цикла разрешён
    Время O(n) и память O(1).
    """
    if not ids:
        return 0
        
    write_index = 1
    for read_index in range(1, len(ids)):
        if ids[read_index] != ids[read_index - 1]:
            ids[write_index] = ids[read_index]
            write_index += 1
            
    del ids[write_index:]
    return write_index


def compress(chars):
    """Сжатие последовательности на месте. Задача 3.

    Серия из одинаковых символов подряд заменяется символом и длиной серии,
    записанной цифрами: ["a", "a", "a", "b"] -> ["a", "3", "b"].
    Серия длины 1 записывается одним символом. Возвращает новую длину.
    Время O(n), память O(1).
    """
    if not chars:
        return 0
        
    write_index = 0
    read_index = 0
    n = len(chars)
    
    while read_index < n:
        char = chars[read_index]
        count = 0
        
        while read_index < n and chars[read_index] == char:
            count += 1
            read_index += 1
            
        chars[write_index] = char
        write_index += 1
        
        if count > 1:
            for digit in str(count):
                chars[write_index] = digit
                write_index += 1
                
    # Отрезаем старый хвост массива, чтобы он соответствовал новой длине
    del chars[write_index:]
    return write_index

def move_zeros(nums):
    """Расширение. Нули переносятся в конец, порядок остальных сохраняется.
    Меняет список на месте и возвращает None.
    Время O(n), память O(1).
    """
    write_index = 0
    for read_index in range(len(nums)):
        if nums[read_index] != 0:
            nums[write_index], nums[read_index] = nums[read_index], nums[write_index]
            write_index += 1
    return None

  

def sorted_squares(nums):
    """Задача 3 из ДЗ - Квадраты отсортированного списка.
  
      Возвращает новый список квадратов по возрастанию за O(n) времени и O(n) памяти.
      Использует метод двух указателей на встречу
      """
    
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    write_index = n - 1

    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2

        if left_square > right_square:
            result[write_index] = left_square
            left += 1
        else:
            result[write_index] = right_square
            right -= 1
        write_index -= 1

    return result