def missing_number(arr):
    arr_sum = sum(arr)
    n = len(arr)
    arithmetic_sum = ((2 + n)/ 2) * (n + 1)

    return int(arithmetic_sum - arr_sum)


print(missing_number([1, 2, 3, 5]))