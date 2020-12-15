n = input('Введите целое число n: ')
n=int(n)

if n > 10:
    print ('Число должно быть однозначным !')
else:
    result = n + n*11 + n*111
    print(result)


