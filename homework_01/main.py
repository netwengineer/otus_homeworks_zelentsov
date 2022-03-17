"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [pow(element, 2) for element in args]


## filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


# [numbers.remove(element) for element in [number for number in numbers if number <= 1]]
# [numbers.remove(element) for element in list(
#     {number for number in numbers for generated_number in range(2, number) if number % generated_number == 0})]

def is_prime(number):
    if number > 1:
        for generated_number in range(2, number):
            if number % generated_number == 0:
                return False
        else:
            return True
    else:
        return False


def filter_numbers(numbers, action):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if action == ODD:
        return [number for number in numbers if number % 2 != 0]
    elif action == EVEN:
        return [number for number in numbers if number % 2 == 0]
    elif action == PRIME:
        return list(filter(is_prime, numbers))
