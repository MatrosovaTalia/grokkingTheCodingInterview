def removeDuplicates(nums) -> int:
    l, r = 0, 1
    while r < len(nums):
        if nums[l] != nums[r]:
            l += 1
            nums[l] = nums[r]  
        r += 1
    return l + 1

print(removeDuplicates([1, 1, 2]))
print(removeDuplicates([2, 2, 3, 3, 3, 3, 9, 1, 1]))