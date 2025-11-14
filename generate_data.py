import numpy as np
import random
import bisect


def generate_sorted(size, start=1):
    if size == 0:
        return []
    arr = [start]
    for _ in range(1, size):
        increment = random.randint(1, 32768)
        arr.append(arr[-1] + increment)
    return arr

def generate_data(tests_num: int):
    print("Generating datasets...")
    for test_num in range(tests_num):
        random.seed(test_num)
        if test_num < 200:
            size = random.randint(1, 100000)
        elif test_num < 400:
            size = random.randint(10001, 1000000)
        else:
            size = random.randint(100001, 10000000)
        pop_size = 2 * size
        if test_num % 2 == 0:
            # No common
            arr_m = generate_sorted(size, 1)
            start_n = arr_m[-1] + 1 if arr_m else 1
            arr_n = generate_sorted(size, start_n)
        else:
            # With common
            arr_m = generate_sorted(size, 1)
            common = random.choice(arr_m)
            arr_n_base = generate_sorted(size - 1, 1)
            pos = bisect.bisect_left(arr_n_base, common)
            arr_n = arr_n_base[:pos] + [common] + arr_n_base[pos:]
        np.save(f'data/{test_num}.npy', (arr_m, arr_n))
        print("generated", test_num)
    print("Datasets generated.")
