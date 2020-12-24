
''' Часть а'''
from itertools import count

for el in count(int(input('Введите число: '))):
    print(el)


''' Часть b'''


from itertools import cycle

my_list = ['qwe', 3332, 0.4, 'hello world']
for el in cycle(my_list):
    print(el)
