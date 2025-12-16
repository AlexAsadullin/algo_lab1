def exponential_search(arr_m, arr_n):
    if len(arr_m) == 0 or len(arr_n) == 0:
        return -1

    if len(arr_m) > len(arr_n):
        arr_m, arr_n = arr_n, arr_m

    M = len(arr_m)
    N = len(arr_n)
    last_found_index = 0

    for i in range(M):
        current_element = arr_m[i]

        if last_found_index >= N or current_element > arr_n[-1]:
            break

        if current_element < arr_n[last_found_index]:
            low = 0
            high = last_found_index - 1
        else:
            low = last_found_index
            high = last_found_index
            step = 1

            while high < N and arr_n[high] < current_element:
                low = high + 1
                high = high + step
                step *= 2

            if high >= N:
                high = N - 1

        if low > high:
            low, high = high, low

        for j in range(low, high + 1):
            if arr_n[j] == current_element:
                return int(current_element)
            elif arr_n[j] > current_element:
                break

        if high < N - 1 and arr_n[high] < current_element:
            last_found_index = high + 1
        else:
            last_found_index = low

    return -1