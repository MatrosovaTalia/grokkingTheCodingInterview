def count_ones(n):
    ones = 0
    mask = 1
    for i in range(32):
        if mask & n != 0:
            ones += 1
        mask <<= 1
    return ones

print(count_ones(0b00000000110000000000010000000000))
