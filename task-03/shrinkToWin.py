def func(num):
    op = 0
    while num > 9:
        digits = [int(digit) for digit in str(num)]
        num = sum(digits)
        op += 1
    return op

num = int(input())
op = func(num)
print(op)