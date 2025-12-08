import time
import tracemalloc
from bisect import bisect_left


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
                return self.arr_m[i], time.perf_counter() - start_time, memory_used
            elif self.arr_m[i] < self.arr_n[j]:
                i += 1
            else:
                j += 1

        peak_memory = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        memory_used = max(peak_memory - start_memory, 1)  # Минимум 1 байт для логарифмической шкалы
        return -1, time.perf_counter() - start_time, memory_used

    def binary_search(self):
        tracemalloc.start()
        start_memory = tracemalloc.get_traced_memory()[1]
        start_time = time.perf_counter()

        if not self.arr_m or not self.arr_n:
            peak_memory = tracemalloc.get_traced_memory()[1]
            tracemalloc.stop()
            memory_used = max(peak_memory - start_memory, 1)  # Минимум 1 байт для логарифмической шкалы
            return -1, time.perf_counter() - start_time, memory_used
        if len(self.arr_m) > len(self.arr_n):
            self.arr_m, self.arr_n = self.arr_n, self.arr_m

        result = next(
            (elem for elem in self.arr_m
             if (idx := bisect_left(self.arr_n, elem)) < len(self.arr_n) and self.arr_n[idx] == elem), # невный цикл while для ускорения (не проходит по органичениям контеста)
            -1
        )

        peak_memory = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        memory_used = max(peak_memory - start_memory, 1)  # Минимум 1 байт для логарифмической шкалы
        return result, time.perf_counter() - start_time, memory_used

    def exponential_search(self):
        tracemalloc.start()
        start_memory = tracemalloc.get_traced_memory()[1]
        start_time = time.perf_counter()

        if not self.arr_m or not self.arr_n:
            peak_memory = tracemalloc.get_traced_memory()[1]
            tracemalloc.stop()
            memory_used = max(peak_memory - start_memory, 1)
            return -1, time.perf_counter() - start_time, memory_used
        lo = max(self.arr_m[0], self.arr_n[0])
        hi = min(self.arr_m[-1], self.arr_n[-1])
        if lo > hi:
            peak_memory = tracemalloc.get_traced_memory()[1]
            tracemalloc.stop()
            memory_used = max(peak_memory - start_memory, 1)
            return -1, time.perf_counter() - start_time, memory_used

        # нижняя граница в self.arr_m
        l = 0
        r = len(self.arr_m) - 1
        i1 = 0
        while l <= r:
            m = (l + r) // 2
            if self.arr_m[m] < lo:
                i1 = m + 1
                l = m + 1
            else:
                r = m - 1

        # верхняя граница в self.arr_m
        l = 0
        r = len(self.arr_m) - 1
        i2 = len(self.arr_m)
        while l <= r:
            m = (l + r) // 2
            if self.arr_m[m] <= hi:
                l = m + 1
            else:
                i2 = m
                r = m - 1

        # нижняя граница в self.arr_n
        l = 0
        r = len(self.arr_n) - 1
        j1 = 0
        while l <= r:
            m = (l + r) // 2
            if self.arr_n[m] < lo:
                j1 = m + 1
                l = m + 1
            else:
                r = m - 1

        # верхняя граница в self.arr_n
        l = 0
        r = len(self.arr_n) - 1
        j2 = len(self.arr_n)
        while l <= r:
            m = (l + r) // 2
            if self.arr_n[m] <= hi:
                l = m + 1
            else:
                j2 = m
                r = m - 1

        found = -1
        ia = i1
        ja = j1
        while ia < i2 and ja < j2:
            x = self.arr_m[ia]
            y = self.arr_n[ja]
            if x == y:
                found = x
                break
            elif x < y:
                ia += 1
            else:
                ja += 1
        peak_memory = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        memory_used = max(peak_memory - start_memory, 1)  # Минимум 1 байт для логарифмической шкалы
        return found, time.perf_counter() - start_time, memory_used

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
