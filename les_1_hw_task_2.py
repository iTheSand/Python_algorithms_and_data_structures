# https://drive.google.com/file/d/1mFQYrqI85LA3Dyv4BQVp16mtV2KYKRB9/view?usp=sharing - diagrams
# Задача 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
# проходящей через эти точки.
x_1 = float(input('х координата 1 точки: '))
y_1 = float(input('y координата 1 точки: '))
x_2 = float(input('х координата 2 точки: '))
y_2 = float(input('y координата 2 точки: '))

if x_1 - x_2 == 0 or y_1 - y_2 == 0:
    print('Нет решений!')
else:
    k = (y_1 - y_2) / (x_1 - x_2)
    b = y_2 - k * x_2
    if b > 0:
        print(f'y = {k}x+{b}')
    else:
        print(f'y = {k}x{b}')
