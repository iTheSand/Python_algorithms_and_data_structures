# Задание 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import Counter

num_of_com = int(input('Введите количество предприятий: '))
result = Counter({})

count = 1
while count <= num_of_com:
    name_com = input(f'Введите название предприятия №{count}: ')
    quarter = 1
    count += 1
    profit_company = 0
    while quarter <= 4:
        quarter_profit = round(float(input(f'Укажите прибыль за {quarter} квартал: ')), 2)
        profit_company += quarter_profit
        quarter += 1
    result[name_com] = profit_company

sum_ave_profit = round(sum(result.values()) / num_of_com, 2)
print()
print(f'Средняя прибыль всех предприятий = {sum_ave_profit} у.е.')

high_profit = []
low_profit = []
for x, y in result.most_common():
    if y >= sum_ave_profit:
        high_profit.append(x)
    else:
        low_profit.append(x)

print('Предприятия, чья прибыль выше среднего:')
print(*high_profit, sep=', ')
print('Предприятия, чья прибыль ниже среднего:')
print(*low_profit, sep=', ')
