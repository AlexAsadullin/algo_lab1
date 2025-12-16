def two_pointers(arr_m: list, arr_n: list) -> int:
    i, j = 0, 0
    while i < len(arr_m) and j < len(arr_n):
        if arr_m[i] == arr_n[j]:
            return arr_m[i]
        elif arr_m[i] < arr_n[j]:
            i += 1
        else:
            j += 1
    return -1