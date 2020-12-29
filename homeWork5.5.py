with open('homeWork5.5.txt', 'w', encoding='UTF-8') as file:
    content = (input('Введите значения:'))
    file.writelines(content)
    result = content.split()

    print(sum(map(int, result)))
