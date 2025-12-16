def recursion(arr: list, start_index: int, target: int) -> int:
    if start_index >= len(arr):
        return -1
    idx = 1
    while start_index + idx < len(arr) and arr[start_index + idx] < target:
        idx *= 2

    l = start_index + (idx // 2)
    r = min(start_index + idx, len(arr) - 1)

    while l <= r:
        m = (l + r) // 2
        if arr[m] == target:
            return m
        elif arr[m] < target:
            l = m + 1
        else:
            r = m - 1
    return l


def exponential_search(arr_m: list, arr_n: list):
    if len(arr_m) == 0 or len(arr_n) == 0:
        return -1

    if len(arr_m) > len(arr_n):
        arr_m, arr_n = arr_n, arr_m
    #M = len(arr_m)
    N = len(arr_n)

    last_found_index = 0
    for i in arr_m:
        found_idnex = recursion(arr_n, last_found_index, i)

        if found_idnex < N and arr_n[found_idnex] == i:
            return True
        last_found_index = found_idnex
        if last_found_index >= N:
            break

    return False
