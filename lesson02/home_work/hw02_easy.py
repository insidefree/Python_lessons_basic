import math
import random
from random import randint
# -*- coding: utf-8 -*-
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка выровненного по правой сторне
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
# Подсказка: использует метод .format()

LIST = ["apple", "banana", "kiwi", "watermelon"]

BIGGER_LENGTH = 0
for l in LIST:
    if BIGGER_LENGTH < len(l):
        BIGGER_LENGTH = len(l)

for l in LIST:
    print('{}.{:{align}{width}}'.format(LIST.index(l) + 1, l, align='>', width=BIGGER_LENGTH + 2))

# Задача-2:
# Даны два произвольные списка. Удалите из первого списка элементы
# присутствующие во втором списке

RANDOM_LIST01 = [int(15 * random.random()) for i in range(0, 15)]
RANDOM_LIST02 = [randint(0, 15) for i in range(0, 15)]
print(RANDOM_LIST01)
print(RANDOM_LIST02)

for el in RANDOM_LIST02:
    if RANDOM_LIST01.count(el) > 0: # I think it's not good solution - because
                                    # in each iteration we search all elements
                                    # in 'list', while we need just get 'true' or 'false'
        RANDOM_LIST01.remove(el)
print(RANDOM_LIST01)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного выполнив следующие условия:
# если элемент кратный двум, то разделить его на 4, если не кратен, то
# умножить на два.

RESULT_LIST = []
for el in RANDOM_LIST01:
    if el%2 == 0:
        RESULT_LIST.append(el/4)
    else:
        RESULT_LIST.append(el*2)

print(RESULT_LIST)
