from random import randint

# Все задачи текущего блока решите с помощью генераторов!

# Задание-1:
# Дан список, заполненный произвольными целыми цифрами, получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

random_list = [randint(-25, 25) for _ in range(10)]
pow_list = [el ** 2 for el in random_list]

print(random_list)
print(pow_list)

# Задание-2:
# Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
fruit_list_01 = ['apple', 'watermelon', 'lemon', 'cherry']
fruit_list_02 = ['pear', 'apple', 'cherry']

result_list = [el_01 for el_01 in fruit_list_01 if el_01 in fruit_list_02]
print("Result that contains elements from several lists is {}".format(result_list))

# Задание-3:
# Дан список, заполненный произвольными числами. Получить список из элементов исходного, удовлетворяющих след. условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

result_list = [el for el in random_list if el % 3 == 0 and el >= 0 and el % 4 != 0]
print("Result list is {}".format(result_list))
