def sortedSquares(nums):
    fp = 0
    squares = []
    while nums[fp] < 0 and fp < len(nums) - 1:
        fp += 1
    l, r = fp - 1, fp
    while len(squares) != len(nums):
        if l >= 0 and r < len(nums):
            if nums[l] ** 2 <= nums[r] ** 2:
                next_el = nums[l] ** 2
                l -= 1
            else:
                next_el = nums[r] ** 2
                r += 1
        elif r >= len(nums):
            next_el = nums[l] ** 2
            l -= 1
        else:
            next_el = nums[r] ** 2
            r += 1
                
        squares.append(next_el)
    return squares

print(sortedSquares([-3, -2, 0, 1, 2, 3, 4]))