def my_func(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Ошибка')
        return

print(my_func(20, 0))
