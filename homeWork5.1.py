file = open('homeWork5.1.txt', 'w', encoding='UTF-8')
while True:
    content = input('Введите значение: ')
    file.write(f'{content} \n')
    if not content:
        break

file.close()

