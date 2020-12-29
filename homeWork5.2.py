with open('homeWork5.1.txt', 'r', encoding='UTF-8') as file:
    content = file.readlines()
    print(f'Кол-во строк в файле: {len(content)}')
    for i, el in enumerate(content):
        print(f'Кол-во символов {i} строки = {len(content[i])}')
