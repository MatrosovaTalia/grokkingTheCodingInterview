def add_two_numbers(a, b):
    x, y = abs(a), abs(b)
    if x < y:
        x, y = y, x
        a, b = b, a
    
    sign = 1 if a > 0 else -1
    same_sign = True if sign == 1 and b >= 0 or sign == -1 and b < 0 else False 
    
    if same_sign:
        while y != 0:
            # addition
            answer = x ^ y
            carry  = (x & y) << 1
            x, y = answer, carry
    else:
        while y != 0:
            # subtraction
            answer = x ^ y
            borrow = ((~x)&y) << 1

            x, y = answer, borrow
    return sign * x

print(add_two_numbers(13, -2))
print(add_two_numbers(15, 2))
print(add_two_numbers(-2, -15))
print(add_two_numbers(2, -13))

