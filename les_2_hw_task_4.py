# https://drive.google.com/file/d/1nDS9TcybrnB1Vgx389jJWbaN5NrQO0x6/view?usp=sharing - diagrams
# Задача 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
num_of_num = int(input('Количество вводимых чисел: '))
count_cycle = 0
search_num = input('Цифра, которую необходимо посчитать: ')
count_num = 0

while num_of_num != count_cycle:
    num = input(f'{count_cycle + 1} - ')
    for i in num:
        if i == search_num:
            count_num += 1
        else:
            pass
    count_cycle += 1
print(f'Цифра {search_num} в введенной последовательности чисел встречается {count_num} раз')
