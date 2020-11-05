# https://drive.google.com/file/d/1nDS9TcybrnB1Vgx389jJWbaN5NrQO0x6/view?usp=sharing - diagrams
# Задача 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
max_num = 0
memory_num = 0

while True:
    sum_num = 0
    num = input('Введите натуральное число (0 - выход) : ')
    if int(num) != 0:
        for i in num:
            sum_num += int(i)
            if sum_num > max_num:
                max_num = sum_num
                memory_num = num
            else:
                pass
    else:
        break

print(f'{memory_num} (число) - {max_num} (сумма цифр)')
