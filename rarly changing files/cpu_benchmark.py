import multiprocessing
import time
import math
from concurrent.futures import ProcessPoolExecutor

def cpu_benchmark_core(core_id):
    """Функция для бенчмарка одного ядра"""
    # Настройка для конкретного ядра
    start_time = time.time()

    # Вычисления для проверки производительности
    total_operations = 0
    for i in range(10**6):  # Многочисленные операции
        # Простая математическая операция
        st = []
        for n in range(2,math.isqrt(i)):
            for d in range(2,n):
                if i%d == 0:
                    st.append(d)
                    st.append(n//d)

        #result = math.sqrt(math.pow(math.log(i+1)//math.cos(i),4)) if i > 0 else 0
        total_operations += 1

    end_time = time.time()

    # Возвращаем результаты
    return {
        "core_id": core_id,
        "operations_per_second": total_operations / (end_time - start_time),
        "time_taken": end_time - start_time,
    }


def cpu_benchmark_parallel():
    """Параллельный бенчмарк на всех ядрах"""
    print("Запуск бенчмарка на всех ядрах...")

    # Получаем количество ядер
    num_cores = multiprocessing.cpu_count()
    print(f"Обнаружено ядер: {num_cores}")

    # Создаем список ядер для тестирования
    cores = list(range(num_cores))

    # Используем ProcessPoolExecutor для параллельных вычислений
    with ProcessPoolExecutor(max_workers=num_cores) as executor:
        # Запускаем бенчмарк на каждом ядре
        results = list(executor.map(cpu_benchmark_core, cores))

    # Вывод результатов
    print("\nРезультаты бенчмарка:")
    for result in results:
        print(
            f"Ядро {result['core_id']}: {result['operations_per_second']:.2f} операций/сек"
        )

    # Общие данные
    total_ops = sum([r["operations_per_second"] for r in results])
    avg_ops = total_ops / len(results)

    print(f"\nСредняя производительность: {avg_ops:.0f} операций/сек")
    print(f"Общая производительность: {total_ops:.0f} операций/сек")

    return results


def cpu_benchmark_single():
    """Одиночный бенчмарк (для сравнения)"""
    print("Запуск одиночного бенчмарка...")

    # Запускаем на одном ядре
    start_time = time.time()
    total_operations = 0

    for i in range(10**6):
        result = math.sqrt(i) + math.log(i + 1) if i > 0 else 0
        total_operations += 1

    end_time = time.time()
    ops_per_sec = total_operations / (end_time - start_time)

    print(f"Одиночное ядро: {ops_per_sec:.2f} операций/сек")
    return ops_per_sec


if __name__ == "__main__":
    # Запуск параллельного бенчмарка
    results = cpu_benchmark_parallel()

    # Сравнение с одиночным режимом
    single_result = cpu_benchmark_single()
