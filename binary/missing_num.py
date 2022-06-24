def missing_num(nums):
    if len(nums) == 1:
        return 0 if nums[0] == 1 else 1

    n = len(nums)
    expected_sum = n * (1 + n) // 2
    return expected_sum - sum(nums)

def xor_missing_num(nums):
    x = len(nums) 
    for n in nums:
        x ^= n
    return x

print(xor_missing_num([0, 1, 4, 3]))

    