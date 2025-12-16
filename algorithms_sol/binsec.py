from bisect import bisect_left

def binary_search(arr_m: list, arr_n: list) -> int:
    if len(arr_m) == 0 or len(arr_n) == 0:
        return -1

    if len(arr_m) > len(arr_n):
        arr_m, arr_n = arr_n, arr_m

    result = next(
        (elem for elem in arr_m
         if (idx := bisect_left(arr_n, elem)) < len(arr_n) and arr_n[idx] == elem),
        -1
    )
    return result