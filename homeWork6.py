a = int(input('Введите результат в 1-ый день пробежки: '))
b = int(input('Введите цель: '))
day = 1
print(f' {day}-й день: {a}')
day=day+1

while a < b:
    a = round(a * 1.1,2)
    print (f' {day}-й день: {a}')
    day = day + 1

a = int(a)
day = day-1 #чот костыль
print (f' На {day}-й день спортсмен достиг результата - не менее {a} км')
