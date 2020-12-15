proceeds = input('Введите значение выручки:  ')
costs = input('Введите значение издержек: ')

proceeds = int(proceeds)
costs = int(costs)

if proceeds > costs:
    print ('Ваша фирма работает в прибыль')
    profit = proceeds - costs
    rental = profit / proceeds
    rental = float(rental)
    print (f' Рентабельность:  {rental}')
    personal = int(input('Введите кол-во сотрудников: '))
    profit2 = profit/personal
    print (f' Прибыль в расчете на 1 сотрудника: {profit2}')

elif proceeds < costs:
    print ('Ваша фирма работает в убыток')