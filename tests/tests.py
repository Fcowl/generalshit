import math


def get_m(n):
    smallest_div = 0
    for d in range(2, math.isqrt(n) + 1):
        if n % d == 0:
            smallest_div = d
            break
    if smallest_div == 0:
        return 0
    largest_div = n // smallest_div
    return smallest_div + largest_div


# Для проверки корректности
def get_divisors(n):
    divisors = set()
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return divisors


def test1():
    divs = sorted(list(get_divisors(5102834)))
    return divs[0] + divs[-1]


def test2():
    return get_m(5102834)


# Результаты будут идентичны
print(f"Результат test1: {test1()}")
print(f"Результат test2: {test2()}")
