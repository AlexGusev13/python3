translate_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
new_line = []

with open('current_file.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()
    for i in lines:
        i = i.split(' ', 1)
        new_line.append(translate_dict[i[0]] + ' ' + i[1])
    print(new_line)

with open('new_file.txt', 'w', encoding='UTF-8') as file:
    file.writelines(new_line)
