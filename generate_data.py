import numpy as np
import random
import bisect


LONG_SIZE = 10_000_000   # ~10 МБ для int64
SHORT_SIZE = 1_000_000   # ~1 МБ для int64


def gen_sorted_random_parity(size: int, start: int = 1, min_step: int = 1, max_step: int = 5) -> np.ndarray:
    """Генерирует отсортированный массив с случайными шагами между элементами."""
    arr = np.empty(size, dtype=np.int64)
    val = start
    for i in range(size):
        arr[i] = val
        term = random.randint(min_step, max_step)
        val += term
    return arr


def gen_sorted_by_parity(size: int, even: bool, start: int = 1, min_step: int = 1, max_step: int = 5) -> np.ndarray:
    """Генерирует отсортированный массив только четных или только нечетных чисел."""
    arr = np.empty(size, dtype=np.int64)
    val = start
    for i in range(size):
        arr[i] = val
        if even:
            term = random.randint(min_step, max_step) * 2
        else:
            term = random.randint(min_step, max_step) * 2 + 1
            
        val += term
    return arr


def pair_odd_odd():
    """Генерирует пару массивов: оба содержат только нечетные числа."""
    long = gen_sorted_by_parity(LONG_SIZE, start=1, even=False)
    short = gen_sorted_by_parity(SHORT_SIZE, start=1, even=False)
    
    np.save("data/odd_odd_short.npy", short)
    np.save("data/odd_odd_long.npy",  long)
    return short, long


def pair_even_odd():
    """Генерирует пару массивов: длинный содержит четные числа, короткий - нечетные."""
    long = gen_sorted_by_parity(LONG_SIZE, start=2, even=True)
    short = gen_sorted_by_parity(SHORT_SIZE, start=1, even=False)
    np.save("data/even_odd_short.npy", short)
    np.save("data/even_odd_long.npy",  long)
    return short, long


def pair_odd_even():
    """Генерирует пару массивов: длинный содержит нечетные числа, короткий - четные."""
    long = gen_sorted_by_parity(LONG_SIZE, start=1, even=False)
    short = gen_sorted_by_parity(SHORT_SIZE, start=2, even=True)
    np.save("data/odd_even_short.npy", short)
    np.save("data/odd_even_long.npy",  long)
    return short, long


def pair_even_even():
    """Генерирует пару массивов: оба содержат только четные числа."""
    long = gen_sorted_by_parity(LONG_SIZE, start=2, even=True)
    short = gen_sorted_by_parity(SHORT_SIZE, start=2, even=True)
    np.save("data/even_even_short.npy", short)
    np.save("data/even_even_long.npy",  long)
    return short, long


def pair_small_long_big_short():
    """Генерирует пару массивов: длинный с маленькими значениями (<100k), короткий с большими (>100k)."""
    long = gen_sorted_random_parity(LONG_SIZE, start=1, max_step=5)
    short = gen_sorted_random_parity(SHORT_SIZE, start=100001, min_step=1, max_step=10)
    np.save("data/small_long_big_short_short.npy", short)
    np.save("data/small_long_big_short_long.npy",  long)
    return short, long


def pair_big_long_small_short():
    """Генерирует пару массивов: длинный с большими значениями (>100k), короткий с маленькими."""
    long = gen_sorted_random_parity(LONG_SIZE, start=100001, min_step=1, max_step=10)
    short = gen_sorted_random_parity(SHORT_SIZE, start=1, max_step=5)
    np.save("data/big_long_small_short_short.npy", short)
    np.save("data/big_long_small_short_long.npy",  long)
    return short, long


def pair_intersecting_ranges():
    """Генерирует пару массивов: нечетные числа от 1 и четные числа от 50000 (частичное пересечение диапазонов)."""
    long = gen_sorted_by_parity(LONG_SIZE, start=1, even=False, max_step=10)  # нечетные: 1,3,5,...~100k
    short = gen_sorted_by_parity(SHORT_SIZE, start=50000, even=True, max_step=10)  # четные: 50000,50002,...~150k
    np.save("data/intersecting_ranges_short.npy", short)
    np.save("data/intersecting_ranges_long.npy", long)
    return short, long


def pair_no_intersection():
    """Генерирует пару массивов: нечетные числа от 1 и четные числа от 100001 (без общих элементов)."""
    long = gen_sorted_by_parity(LONG_SIZE, start=1, even=False, max_step=5)
    short = gen_sorted_by_parity(SHORT_SIZE, start=100001, even=True, max_step=5)
    np.save("data/no_intersection_short.npy", short)
    np.save("data/no_intersection_long.npy", long)
    return short, long


def pair_identical_values():
    """Генерирует пару идентичных массивов с одинаковыми значениями."""
    base = gen_sorted_by_parity(SHORT_SIZE, start=1, even=False, max_step=10)
    long = base.copy()
    short = base.copy()
    np.save("data/identical_values_short.npy", short)
    np.save("data/identical_values_long.npy", long)
    return short, long


def pair_single_element():
    """Генерирует пару массивов: один обычный, второй содержит всего один элемент."""
    long = gen_sorted_by_parity(LONG_SIZE, start=1, even=False, max_step=5)
    short = np.array([1000], dtype=np.int64)
    np.save("data/single_element_short.npy", short)
    np.save("data/single_element_long.npy", long)
    return short, long


def pair_empty_array():
    """Генерирует пару массивов: один обычный, второй пустой."""
    long = gen_sorted_by_parity(LONG_SIZE, start=1, even=False, max_step=5)
    short = np.array([], dtype=np.int64)
    np.save("data/empty_array_short.npy", short)
    np.save("data/empty_array_long.npy", long)
    return short, long


def pair_extreme_size_difference():
    """Генерирует пару массивов с экстремальной разницей в размерах (100M vs 10 элементов)."""
    long = gen_sorted_by_parity(100_000_000, start=1, even=False, max_step=2)
    short = gen_sorted_by_parity(10, start=1, even=False, max_step=5)
    np.save("data/extreme_size_short.npy", short)
    np.save("data/extreme_size_long.npy", long)
    return short, long


def pair_sequential_overlap():
    """Генерирует пару массивов: нечетные от 1 и четные от 2 (смежные диапазоны без пересечения)."""
    long = gen_sorted_by_parity(LONG_SIZE, start=1, even=False, max_step=2)
    short = gen_sorted_by_parity(SHORT_SIZE, start=2, even=True, max_step=2)
    np.save("data/sequential_overlap_short.npy", short)
    np.save("data/sequential_overlap_long.npy", long)
    return short, long


def pair_both_empty():
    """Генерирует пару пустых массивов."""
    long = np.array([], dtype=np.int64)
    short = np.array([], dtype=np.int64)
    np.save("data/both_empty_short.npy", short)
    np.save("data/both_empty_long.npy", long)
    return short, long