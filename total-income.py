from re import findall
from typing import Callable


def generator_numbers(text_to_scan: str):
    # Задаємо патерн та шукаємо числа з плаваючою точкою.
    pattern = r"\d+[.,]?\d+"
    salaries = findall(pattern, text_to_scan)
    for salary in salaries:
        # В циклі перетворюємо знайдені числа у флоат та видаляємо можливі пробіли.
        salary = float(salary.strip())
        # повертаємо число з генератора.
        yield salary


def sum_profit(text_to_scan: str, func: Callable) -> float:
    # Повертаємо суму чисел.
    return sum(func(text_to_scan))


text = "Загальний дохід працівника складає  ться з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
# Обчислюємо загальний дохід
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")