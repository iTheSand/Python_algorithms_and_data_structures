# https://drive.google.com/file/d/1nDS9TcybrnB1Vgx389jJWbaN5NrQO0x6/view?usp=sharing - diagrams
# Задача 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def count_dig(num):
    num = str(num)
    even = ''
    not_even = ''
    for i in num:
        if int(i) % 2 == 0:
            even += str(i)
        else:
            not_even += str(i)
    return (f'четных цифр - {len(even)}, не четных цифр - {len(not_even)}')


print(count_dig(34560))
