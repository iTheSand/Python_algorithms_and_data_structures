# https://drive.google.com/file/d/1mFQYrqI85LA3Dyv4BQVp16mtV2KYKRB9/view?usp=sharing - diagrams
# Задача 9. Вводятся три разных числа.
# Найти, какое из них является средним (больше одного, но меньше другого).
print('Введите 3 разных числа!')
a = int(input('Введите первое целое число: '))
b = int(input('Введите второе целое число: '))
c = int(input('Введите третье целое число: '))

if a > b and a < c or a > c and a < b:
    print(f'{a} является средним числом!')
else:
    if b > a and b < c or b > c and b < a:
        print(f'{b} является средним числом!')
    else:
        print(f'{c} является средним числом!')
