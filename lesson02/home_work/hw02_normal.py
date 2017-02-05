from math import sqrt
from random import randint

# Задача-1:
# Дан список заполненный произвольными целыми числами, получите новый список элементами которого будут
# квадратные корни элементов исходного списка, но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
RANDOM_LIST = [randint(-64, 64) for i in range(0, 50)]
RESULT_LIST = []

for el in RANDOM_LIST:
    if el > 0 and sqrt(el) % 2 == 0:
        RESULT_LIST.append(el**2)
print(RANDOM_LIST)
print(RESULT_LIST)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
DAYS = {
    '01': 'first',
    '02': 'second',
    '03': 'third',
    '04': 'fourth',
    '05': 'fifth',
    '06': 'sixth',
    '07': 'seventh',
    '08': 'eighth',
    '09': 'ninth',
    '10': 'tenth',
    '11': 'eleventh',
    '12': 'twelfth',
    '13': 'thirteenth',
    '14': 'fourteenth',
    '15': 'fifteenth ',
    '16': 'sixteenth ',
    '17': 'seventeenth',
    '18': 'eighteenth',
    '19': 'nineteenth',
    '20': 'twenty',
    '21': 'twenty first',
    '22': 'twenty second',
    '23': 'twenty third',
    '24': 'twenty fourth',
    '25': 'twenty fifth',
    '26': 'twenty sixth',
    '27': 'twenty seventh',
    '28': 'twenty eighth',
    '29': 'twenty ninth',
    '30': 'thirty',
    '31': 'thirty first'
}

MONTHS = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
}

while True:
    CUSTOM_DATE = input('Enter date in format dd.mm.yyyy: ').split('.')
    if len(CUSTOM_DATE) == 3 and int(CUSTOM_DATE[0]) in range(1, 32) and int(CUSTOM_DATE[1]) in range(1, 13) and int(CUSTOM_DATE[2]) in range(1, 9999):
        print('{} {} {} years'.format(DAYS[CUSTOM_DATE[0]], MONTHS[CUSTOM_DATE[1]], CUSTOM_DATE[2]))
        break
    else:
        print('Enter correct date in format dd.mm.yyyy, please...')

# Задача-3: Напишите алгоритм заполняющий список произвольными целыми числами в диапазоне от -100 до 100
# В списке должно быть n - элементов
# Подсказка: для получения случайного числа изпользуйте функцию randint()
# модуля random
N = int(input('Enter count of list: '))
RANDOM_LIST_100 = [randint(-100, 100) for i in range(0, N)]
print(RANDOM_LIST_100)

# Задача-4: Дан список заполненный произвольными целыми числами
# Получите новый список, элементами которого будут только уникальные
# элементы исходного
UNIQ_LIST = []
for el in RANDOM_LIST_100:
    if RANDOM_LIST_100.count(el) == 1:
        UNIQ_LIST.append(el)

print(UNIQ_LIST)
