from sys import argv

script_name, work_time, payment_hour, premium = argv

print(f'Заработная плата сотрудника: {int(work_time) * int(payment_hour) + int(premium)}  рублей ')