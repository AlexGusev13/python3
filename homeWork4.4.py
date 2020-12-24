input_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 1, 78, 78, 123, 55]

output_list = [el for i, el in enumerate(input_list) if input_list[i-1] != input_list[i]]

print(f'Исходный список: {input_list}')
print(f'Результат: {output_list}')