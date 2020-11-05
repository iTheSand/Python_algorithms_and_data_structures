# https://drive.google.com/file/d/1nDS9TcybrnB1Vgx389jJWbaN5NrQO0x6/view?usp=sharing - diagrams
# Задача 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.
# p.s.: моя первая рекурсия)
# с диаграммой возникли трудности из-за вложенной функции...

def inverse_num(num):
    inv_num = ''
    counter = 0

    def last_num(num):
        nonlocal inv_num, counter
        length_num = len(str(num)) - counter
        for count_iter, i in enumerate(str(num), 1):
            if length_num == count_iter and length_num > 0:
                inv_num += i
                counter += 1
                return last_num(num)
            else:
                pass

    last_num(num)
    return int(inv_num)


if __name__ == '__main__':
    a = int(input('Введите любое натуральное число: '))
    b = inverse_num(a)
    print(f'обратное число - {b}')
