# https://drive.google.com/file/d/1mFQYrqI85LA3Dyv4BQVp16mtV2KYKRB9/view?usp=sharing - diagrams
# Задача 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
from functools import reduce

a = input('введите положительное трехзначное число: ')
if int(a) > 99 and int(a) < 1000:
    b = sum(map(int, list(a)))
    c = reduce(lambda x, y: x * y, map(int, list(a)))
    print(f'сумма - {b}, произведение - {c}')
else:
    print('Нет решений!')
