def count_bits(n):
    ans = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        num = i
        while num != 0:
            ans[i] += 1
            num &= (num - 1)

    return ans


def count_bits_on(n):
    ans = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        num = i
        ans[i] = ans[i & (i - 1)] + 1

    return ans


print(count_bits_on(5))

# 5 
# ans = [0 0 0 0 0 0] O(n)
# num = 1; ans[1] = 1; num = 0; endwhile

# ans = [0 1 0 0 0 0]
# num = 2; ans = 1; num = 10 & 01 = 0; endwhile

# ans = [0 1 1 0 0 0]
# num = 3; ans = 1; num = 11 & 10 = 1; ans = 2; num = 10 & 01; endwhile

# ans = [0 1 1 2 0 0] 
# num = 4 ans = 1 num = 100 & 11; endwhile

# ans = [0 1 1 2 1 0]
# num = 5 ans = 1 num = 101 & 100; ans = 2 num = 100 & 11; endwhile

# return [0 1 1 2 1 2]


