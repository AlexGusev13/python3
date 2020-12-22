def my_func(a, b ,c):
    if a >= c <= b:
        return a + b
    elif b >= a <= c:
        return b + c
    else:
        return c + a
print(my_func(10, 20, 3))

