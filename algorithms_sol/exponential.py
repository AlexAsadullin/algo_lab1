def exponential_search(arr_m: list, arr_n: list) -> int:
    if not arr_m or not arr_n:
        return -1
    if len(arr_m) > len(arr_n):
        arr_m, arr_n = arr_n, arr_m

    if max(arr_m) < min(arr_n):
        return -1

    last_index = 0

    for x in arr_m:
        if last_index >= len(arr_n):
            break
        if x > arr_n[-1]:
            break

        idx = 1
        while last_index + idx < len(arr_n) and arr_n[last_index + idx] < x:
            idx *= 2

        left = last_index + (idx // 2)
        right = min(last_index + idx, len(arr_n) - 1)

        while left <= right:
            mid = (left + right) // 2
            if arr_n[mid] == x:
                return x
            elif arr_n[mid] < x:
                left = mid + 1
            else:
                right = mid - 1

        last_index = left

    return -1