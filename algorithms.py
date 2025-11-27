import time
import tracemalloc


def exponential_search(arr, target):
    if len(arr) == 0:
        return False
    if arr[0] == target:
        return True
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2
    left = i // 2
    right = min(i, len(arr) - 1)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


class Solution:
    def __init__(self, arr_m, arr_n):
        self.arr_m = arr_m
        self.arr_n = arr_n

    def two_pointers(self):
        tracemalloc.start()
        start_memory = tracemalloc.get_traced_memory()[1]
        start_time = time.perf_counter()

        i, j = 0, 0
        while i < len(self.arr_m) and j < len(self.arr_n):
            if self.arr_m[i] == self.arr_n[j]:
                peak_memory = tracemalloc.get_traced_memory()[1]
                tracemalloc.stop()
                memory_used = max(peak_memory - start_memory, 1)  # Минимум 1 байт для логарифмической шкалы
                return True, time.perf_counter() - start_time, memory_used
            elif self.arr_m[i] < self.arr_n[j]:
                i += 1
            else:
                j += 1

        peak_memory = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        memory_used = max(peak_memory - start_memory, 1)  # Минимум 1 байт для логарифмической шкалы
        return False, time.perf_counter() - start_time, memory_used

    def binary_search(self):
        tracemalloc.start()
        start_memory = tracemalloc.get_traced_memory()[1]
        start_time = time.perf_counter()

        for elem in self.arr_m:
            left, right = 0, len(self.arr_n) - 1
            while left <= right:
                mid = (left + right) // 2
                if self.arr_n[mid] == elem:
                    peak_memory = tracemalloc.get_traced_memory()[1]
                    tracemalloc.stop()
                    memory_used = max(peak_memory - start_memory, 1)  # Минимум 1 байт для логарифмической шкалы
                    return True, time.perf_counter() - start_time, memory_used
                elif self.arr_n[mid] < elem:
                    left = mid + 1
                else:
                    right = mid - 1

        peak_memory = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        memory_used = max(peak_memory - start_memory, 1)  # Минимум 1 байт для логарифмической шкалы
        return False, time.perf_counter() - start_time, memory_used

    def exponential_search(self):
        tracemalloc.start()
        start_memory = tracemalloc.get_traced_memory()[1]
        start_time = time.perf_counter()

        for elem in self.arr_m:
            if exponential_search(self.arr_n, elem):
                peak_memory = tracemalloc.get_traced_memory()[1]
                tracemalloc.stop()
                memory_used = max(peak_memory - start_memory, 1)  # Минимум 1 байт для логарифмической шкалы
                return True, time.perf_counter() - start_time, memory_used

        peak_memory = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        memory_used = max(peak_memory - start_memory, 1)  # Минимум 1 байт для логарифмической шкалы
        return False, time.perf_counter() - start_time, memory_used

    def binary_divide(self):
        tracemalloc.start()
        start_memory = tracemalloc.get_traced_memory()[1]
        start_time = time.perf_counter()

        def _has_common(i1, j1, i2, j2):
            if i1 >= j1 or i2 >= j2:
                return False
            mid = (i1 + j1) // 2
            val = self.arr_m[mid]
            l, r = i2, j2 - 1
            while l <= r:
                m = (l + r) // 2
                if self.arr_n[m] == val:
                    return True
                elif self.arr_n[m] < val:
                    l = m + 1
                else:
                    r = m - 1
            pos = l
            if _has_common(i1, mid, i2, pos):
                return True
            if _has_common(mid + 1, j1, pos, j2):
                return True
            return False

        res = _has_common(0, len(self.arr_m), 0, len(self.arr_n))
        peak_memory = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        memory_used = max(peak_memory - start_memory, 1)  # Минимум 1 байт для логарифмической шкалы
        return res, time.perf_counter() - start_time, memory_used
