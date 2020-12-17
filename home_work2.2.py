list = [1, 6, 4, 5]
i = 0

while len(list) < 10:
    n = int(input('Введите новый элемент массива: '))
    list.append(n)
    for i in range(0, len(list) - 1, 2):
        list[i], list[i+1] = list[i+1], list[i]
    print(list)