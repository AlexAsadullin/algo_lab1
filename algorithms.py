import time
import tracemalloc
from bisect import bisect_left
import math

class Solution:
    def __init__(self, arr_m, arr_n):
        self.arr_m = arr_m
        self.arr_n = arr_n

    def two_pointers(self):
        tracemalloc.start()
        start_memory = tracemalloc.get_traced_memory()[0]
        start_time = time.perf_counter()

        i, j = 0, 0
        while i < len(self.arr_m) and j < len(self.arr_n):
            if self.arr_m[i] == self.arr_n[j]:
                peak_memory = tracemalloc.get_traced_memory()[0]
                tracemalloc.stop()
                memory_used = max(peak_memory - start_memory, 0)
                return self.arr_m[i], time.perf_counter() - start_time, memory_used
            elif self.arr_m[i] < self.arr_n[j]:
                i += 1
            else:
                j += 1

        peak_memory = tracemalloc.get_traced_memory()[0]
        tracemalloc.stop()
        memory_used = max(peak_memory - start_memory, 0)
        return -1, time.perf_counter() - start_time, memory_used

    def binary_search(self):
        tracemalloc.start()
        start_memory = tracemalloc.get_traced_memory()[0]
        start_time = time.perf_counter()

        if len(self.arr_m) == 0 or len(self.arr_n) == 0:
            peak_memory = tracemalloc.get_traced_memory()[0]
            tracemalloc.stop()
            memory_used = max(peak_memory - start_memory, 0)
            return -1, time.perf_counter() - start_time, memory_used

        if len(self.arr_m) > len(self.arr_n):
            self.arr_m, self.arr_n = self.arr_n, self.arr_m

        result = next(
            (elem for elem in self.arr_m
             if (idx := bisect_left(self.arr_n, elem)) < len(self.arr_n) and self.arr_n[idx] == elem),
            -1
        )

        peak_memory = tracemalloc.get_traced_memory()[0]
        tracemalloc.stop()
        memory_used = max(peak_memory - start_memory, 0)
        return result, time.perf_counter() - start_time, memory_used

    def exponential_search(self):
        """Версия с оптимальной сложностью O(M log(2N/M)) для поиска общего элемента"""
        tracemalloc.start()
        start_memory = tracemalloc.get_traced_memory()[0]
        start_time = time.perf_counter()

        found = -1  # Значение по умолчанию, если общий элемент не найден

        if len(self.arr_m) == 0 or len(self.arr_n) == 0:
            peak_memory = tracemalloc.get_traced_memory()[0]
            tracemalloc.stop()
            memory_used = max(peak_memory - start_memory, 0)
            return found, time.perf_counter() - start_time, memory_used

        if len(self.arr_m) > len(self.arr_n):
            self.arr_m, self.arr_n = self.arr_n, self.arr_m
            print("swap done")
        else:
            print("swap skipped")

        # M - длина меньшего массива, N - длина большего массива
        M = len(self.arr_m)
        N = len(self.arr_n)

        # Начинаем поиск с начала большего массива
        last_found_index = 0

        for i in range(M):
            current_element = self.arr_m[i]

            # Если текущий элемент больше последнего элемента большего массива - дальше искать бесполезно
            if last_found_index >= N or current_element > self.arr_n[-1]:
                break

            # Если текущий элемент меньше, чем элемент в last_found_index,
            # то мы можем начать поиск с начала, но с учетом монотонности это маловероятно
            if last_found_index < N and current_element < self.arr_n[last_found_index]:
                # В этом случае ищем в диапазоне [0, last_found_index]
                low = 0
                high = last_found_index - 1
            else:
                # Экспоненциальный поиск для нахождения верхней границы
                low = last_found_index
                high = last_found_index
                step = 1

                # Удваиваем шаг пока не выйдем за границы или не найдем элемент >= current_element
                while high < N and self.arr_n[high] < current_element:
                    low = high + 1
                    high = last_found_index + step
                    if high >= N:
                        high = N - 1
                        break
                    step *= 2

            # Если текущий элемент точно больше всех оставшихся элементов - выходим
            if low >= N or (low < N and current_element < self.arr_n[low]):
                continue

            # Если верхняя граница вышла за пределы - устанавливаем на последний элемент
            if high >= N:
                high = N - 1

            # Если после экспоненциального поиска диапазон некорректный - корректируем
            if low > high:
                low, high = high, low

            # Бинарный поиск в найденном диапазоне
            while low <= high:
                mid = (low + high) // 2
                if self.arr_n[mid] == current_element:
                    found = current_element
                    peak_memory = tracemalloc.get_traced_memory()[0]
                    tracemalloc.stop()
                    memory_used = max(peak_memory - start_memory, 0)
                    return found, time.perf_counter() - start_time, memory_used
                elif self.arr_n[mid] < current_element:
                    low = mid + 1
                else:
                    high = mid - 1

            # Обновляем last_found_index для следующего поиска
            # Если мы дошли до high и все элементы были меньше current_element,
            # то начинаем следующий поиск с high + 1
            if high < N - 1 and self.arr_n[high] < current_element:
                last_found_index = high + 1
            # Если мы нашли позицию где элементы становятся больше current_element,
            # то начинаем следующий поиск с этой позиции
            elif low < N:
                last_found_index = low
            else:
                last_found_index = N  # Достигли конца массива

        peak_memory = tracemalloc.get_traced_memory()[0]
        tracemalloc.stop()
        memory_used = max(peak_memory - start_memory, 0)
        return found, time.perf_counter() - start_time, memory_used

    def binary_divide(self):
        tracemalloc.start()
        start_memory = tracemalloc.get_traced_memory()[0]
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
        peak_memory = tracemalloc.get_traced_memory()[0]
        tracemalloc.stop()
        memory_used = max(peak_memory - start_memory, 0)
        return res, time.perf_counter() - start_time, memory_used