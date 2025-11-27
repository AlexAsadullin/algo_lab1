import numpy as np
import random
import bisect


LONG_SIZE = 10_000_000   # ~10 МБ для int64
SHORT_SIZE = 1_000_000   # ~1 МБ для int64


def gen_sorted_random_parity(size: int, start: int = 1, min_step: int = 1, max_step: int = 5) -> np.ndarray:
    arr = np.empty(size, dtype=np.int64)
    val = start
    for i in range(size):
        arr[i] = val
        term = random.randint(min_step, max_step)
        val += term
    return arr


def gen_sorted_by_parity(size: int, even: bool, start: int = 1, min_step: int = 1, max_step: int = 5) -> np.ndarray:
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
    long = gen_sorted_by_parity(LONG_SIZE, start=1, even=False)
    short = gen_sorted_by_parity(SHORT_SIZE, start=1, even=False)
    
    np.save("data/odd_odd_short.npy", short)
    np.save("data/odd_odd_long.npy",  long)
    return short, long


def pair_even_odd():
    long = gen_sorted_by_parity(LONG_SIZE, start=2, even=True)
    short = gen_sorted_by_parity(SHORT_SIZE, start=1, even=False)
    np.save("data/even_odd_short.npy", short)
    np.save("data/even_odd_long.npy",  long)
    return short, long


def pair_odd_even():
    long = gen_sorted_by_parity(LONG_SIZE, start=1, even=False)
    short = gen_sorted_by_parity(SHORT_SIZE, start=2, even=True)
    np.save("data/odd_even_short.npy", short)
    np.save("data/odd_even_long.npy",  long)
    return short, long


def pair_even_even():
    long = gen_sorted_by_parity(LONG_SIZE, start=2, even=True)
    short = gen_sorted_by_parity(SHORT_SIZE, start=2, even=True)
    np.save("data/even_even_short.npy", short)
    np.save("data/even_even_long.npy",  long)
    return short, long


def pair_small_long_big_short():
    long = gen_sorted_by_parity(LONG_SIZE, start=1, max_step=5)                # остаёмся < 100000
    short = gen_sorted_by_parity(SHORT_SIZE, start=100001, min_step=1, max_step=10)
    np.save("data/small_long_big_short_short.npy", short)
    np.save("data/small_long_big_short_long.npy",  long)
    return short, long


def pair_big_long_small_short():
    long = gen_sorted_by_parity(LONG_SIZE, start=100001, min_step=1, max_step=10)
    short = gen_sorted_by_parity(SHORT_SIZE, start=1, max_step=5)
    np.save("data/big_long_small_short_short.npy", short)
    np.save("data/big_long_small_short_long.npy",  long)
    return short, long
