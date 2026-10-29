import time
import multiprocessing
import concurrent.futures
from typing import List, Tuple
import numpy as np
from functools import partial
import os


def fibonacci_recursive(n: int) -> int:
    """Рекурсивная реализация вычисления чисел Фибоначчи"""
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n: int) -> int:
    """Итеративная реализация вычисления чисел Фибоначчи"""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_memoization(n: int, memo: dict = {}) -> int:
    """Реализация с мемоизацией"""
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]


def fibonacci_matrix(n: int) -> int:
    """Матричный метод для вычисления чисел Фибоначчи"""
    if n <= 1:
        return n

    def matrix_power(matrix, power):
        if power == 1:
            return matrix
        if power % 2 == 0:
            half = matrix_power(matrix, power // 2)
            return np.dot(half, half)
        else:
            return np.dot(matrix_power(matrix, power - 1), matrix)

    # Матрица [[1, 1], [1, 0]]
    base_matrix = np.array([[1, 1], [1, 0]])
    result_matrix = matrix_power(base_matrix, n - 1)
    return result_matrix[0, 0]


def benchmark_single(func, *args, iterations: int = 100) -> Tuple[float, float]:
    """Функция для бенчмарка производительности с одним ядром"""
    times = []
    results = []
    for _ in range(iterations):
        start_time = time.perf_counter()
        result = func(*args)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
        results.append(result)
    avg_time = sum(times) / len(times)
    return avg_time, results[0]


def benchmark_multi(
    func, *args, iterations: int = 100, num_processes: int = 4
) -> Tuple[float, float]:
    """Функция для бенчмарка производительности с несколькими процессами"""
    # Создаем пулы процессов
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_processes) as executor:
        # Выполняем функцию в параллель
        futures = [executor.submit(func, *args) for _ in range(num_processes)]
        results = [future.result() for future in futures]

    # Собираем время выполнения
    times = []
    for _ in range(iterations):
        start_time = time.perf_counter()
        result = func(*args)
        end_time = time.perf_counter()
        times.append(end_time - start_time)

    avg_time = sum(times) / len(times)
    return avg_time, results[0] if results else 0


def benchmark_cpu(func, n: int, iterations: int = 100) -> Tuple[float, float]:
    """Функция для бенчмарка производительности по CPU"""
    start_time = time.perf_counter()
    result = func(n)
    end_time = time.perf_counter()
    return (end_time - start_time), result


def run_benchmark():
    """Запуск бенчмарка для больших чисел и всех ядер"""
    print("Бенчмарк вычисления чисел Фибоначчи")
    print("=" * 70)
    print("Тестирование для больших чисел и всех ядер")
    print("=" * 70)

    # Тестовые значения (большие числа)
    test_values = [30, 35, 40]

    # Получаем количество ядер
    num_cores = multiprocessing.cpu_count()
    print(f"Количество ядер: {num_cores}")

    # Создаем список ядер
    cores = list(range(num_cores))

    for n in test_values:
        print(f"\nТестирование для n={n}:")

        # Рекурсивная версия (медленная)
        try:
            recursive_time, _ = benchmark_cpu(fibonacci_recursive, n, iterations=10)
            print(f"Рекурсивная: {recursive_time:.6f} секунд")
        except RecursionError:
            print("Рекурсивная: ошибка (слишком глубокий рекурсивный вызов)")

        # Итеративная версия
        iterative_time, _ = benchmark_cpu(fibonacci_iterative, n, iterations=100)
        print(f"Итеративная: {iterative_time:.6f} секунд")

        # Версия с мемоизацией
        memoization_time, _ = benchmark_cpu(fibonacci_memoization, n, iterations=100)
        print(f"Мемоизация: {memoization_time:.6f} секунд")

        # Матричный метод
        matrix_time, _ = benchmark_cpu(fibonacci_matrix, n, iterations=100)
        print(f"Матричный метод: {matrix_time:.6f} секунд")

        # Параллельное выполнение
        try:
            # Используем multiprocessing для параллельного выполнения
            start_time = time.perf_counter()
            with multiprocessing.Pool(processes=num_cores) as pool:
                results = pool.map(fibonacci_iterative, [n] * num_cores)
            end_time = time.perf_counter()
            print(
                f"Параллельное выполнение ({num_cores} ядер): {end_time - start_time:.6f} секунд"
            )
        except Exception as e:
            print(f"Ошибка параллельного выполнения: {e}")


def run_advanced_benchmark():
    """Расширенный бенчмарк для всех ядер и больших чисел"""
    print("\n" + "=" * 70)
    print("Расширенный бенчмарк для всех ядер и больших чисел")
    print("=" * 70)

    # Тестовые значения
    test_values = [30]

    # Получаем количество ядер
    num_cores = multiprocessing.cpu_count()
    print(f"Количество ядер: {num_cores}")

    for n in test_values:
        print(f"\nТестирование для n={n}:")

        # Запускаем методы с использованием разных ядер
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_cores) as executor:
            # Многопоточное выполнение
            threads = [
                executor.submit(fibonacci_recursive, n) for _ in range(num_cores)
            ]
            results = [thread.result() for thread in threads]
            print(
                f"Многопоточное выполнение ({num_cores} потоков): {results[0] if results else 0}"
            )

        # Параллельные вычисления
        try:
            # Используем multiprocessing для параллельных вычислений
            start_time = time.perf_counter()
            with multiprocessing.Pool(processes=num_cores) as pool:
                results = pool.map(fibonacci_iterative, [n] * num_cores)
            end_time = time.perf_counter()
            print(
                f"Параллельные вычисления ({num_cores} процессов): {end_time - start_time:.6f} секунд"
            )
        except Exception as e:
            print(f"Ошибка параллельных вычислений: {e}")


if __name__ == "__main__":
    # Запуск основного бенчмарка
    #run_benchmark()

    # Запуск расширенного бенчмарка
    run_advanced_benchmark()
