import time
import tracemalloc
import os
import psutil

from algorithms_sol.two_pointers import two_pointers
from algorithms_sol.binsec import binary_search
from algorithms_sol.exponential import exponential_search
from algorithms_sol.binary_divide import binary_divide


NUM_TESTS_FOR_TIME = 100

class Solution:
    def __init__(self, arr_m, arr_n):
        self.arr_m = arr_m
        self.arr_n = arr_n

    def two_pointers(self):
        process = psutil.Process(os.getpid())

        tracemalloc.start()
        before_mem = process.memory_info().rss
        res = two_pointers(self.arr_m, self.arr_n)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        after_mem = process.memory_info().rss
        memory_used = max(peak / 1024, after_mem - before_mem) # kbytes

        start = time.perf_counter()
        for _ in range(NUM_TESTS_FOR_TIME):
            two_pointers(self.arr_m, self.arr_n)
        time_spent = (time.perf_counter() - start) / NUM_TESTS_FOR_TIME

        return res, time_spent, memory_used

    def binary_search(self):
        process = psutil.Process(os.getpid())

        tracemalloc.start()
        before_mem = process.memory_info().rss
        res = binary_search(self.arr_m, self.arr_n)

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        after_mem = process.memory_info().rss
        memory_used = max(peak / 1024, after_mem - before_mem)  # kbytes

        start = time.perf_counter()
        for _ in range(NUM_TESTS_FOR_TIME):
            binary_search(self.arr_m, self.arr_n)
        time_spent = (time.perf_counter() - start) / NUM_TESTS_FOR_TIME

        return res, time_spent, memory_used

    def exponential_search(self):
        process = psutil.Process(os.getpid())

        tracemalloc.start()
        before_mem = process.memory_info().rss
        res = exponential_search(self.arr_m, self.arr_n)

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        after_mem = process.memory_info().rss
        memory_used = max(peak / 1024, after_mem - before_mem)  # kbytes

        start = time.perf_counter()
        for _ in range(10):
            exponential_search(self.arr_m, self.arr_n)
        time_spent = (time.perf_counter() - start) / 10

        return res, time_spent, memory_used

    def binary_divide(self):
        process = psutil.Process(os.getpid())

        tracemalloc.start()
        before_mem = process.memory_info().rss
        res = binary_divide(self.arr_m, self.arr_n)

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        after_mem = process.memory_info().rss
        memory_used = max(peak / 1024, after_mem - before_mem)  # kbytes

        start = time.perf_counter()
        for _ in range(NUM_TESTS_FOR_TIME):
            binary_divide(self.arr_m, self.arr_n)
        time_spent = (time.perf_counter() - start) / NUM_TESTS_FOR_TIME

        return res, time_spent, memory_used