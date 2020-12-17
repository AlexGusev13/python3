request = input('Введите предложение: ').split()

for i, el in enumerate(request):
    print(f'{i+1}: {el[:10]}')
