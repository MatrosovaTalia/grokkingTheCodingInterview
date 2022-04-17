def move_zeroes(nums):
    if len(nums) == 1:
        return nums
    
    # r = read index, w = write index
    r = w = len(nums) - 1

    while r >= 0:
        if nums[r] != 0:
            nums[w] = nums[r]
            w -= 1
        r -= 1
    
    for i in range(0, w + 1):
        nums[i] = 0
    return nums

print(move_zeroes([1, 0, 2, 0, 3, 0, 4, 0]))
print(move_zeroes([1, 0, 2, 0, 0, 0, 3, 0, 4, 0]))
print(move_zeroes([1, 0, 2, 0, 3, 0, 4]))
print(move_zeroes([1, 2, 3, 4]))
print(move_zeroes([0, 0, 0, 0]))