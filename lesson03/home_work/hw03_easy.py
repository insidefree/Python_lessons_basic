# Задание-1:
# Напишите функцию округлящую полученное произвольное десятичное число,
# до кол-ва знаков (кол-во знаков передается вторым аргументом)
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные и функции и функции из
# модуля math


def my_round(number, ndigits):
    ls = list(str(number).split("."))
    if int(ls[1][ndigits]) < 5:
        return float(ls[0] + "." + ls[1][ndigits-1])
    else:
        return float(ls[0] + "." + ls[1])


print(my_round(2.1234547, 5))

# Задание-2:
# Дан шестизначный номер билета, определить является ли билет счасливым
# Решение реализовать в виде функции
# Билет считается счастливым, если сумма его первых и последних цифр равны
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    count = len(list(str(ticket_number)))
    part1 = 0
    part2 = 0
    if count % 2 == 0:
        count = int(count / 2)
        ls = list(str(ticket_number))
        while count > 0:
            part1 += int(ls[count-1])
            part2 += int(ls[-count])
            count -= 1
        return True
    else:
        return False

lucky_ticket(123321)
