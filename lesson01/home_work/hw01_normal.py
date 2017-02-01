# Задача-1: Дано произвольное целое число, вывести самую большую цифру
# этого числа
number = 123865748021
result = 0
while number:
    number = number // 10
    result = number % 10 if result < number % 10 else result
print(result)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу используя только две переменные
numberA = int(input("numberA = "))
numberB = int(input("numberB = "))
numberA = numberA + numberB
numberB = numberB - numberA
numberB = -numberB
numberA = numberA - numberB
print("numberA = ", numberA, "numberB = ", numberB)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида ax2 + bx + c = 0.
# Для вычисления квадратного корня воспользуйтесь функицй sqrt() молудя math
# import math
# math.sqrt(4) - вычисляет корень числа 4
import math
print(" *** Hi, I am a program that can help you with \"quadratic equation\" like (ax2 + bx + c = 0)")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = b**2 - 4 * a * c
x1 = 0
x2 = 0
print("Discriminant = ", d)
if d > 0:
    x1 = (-b + math.sqrt(b**2 - 4 * a * c)) / 2 * a
    x2 = (-b - math.sqrt(b**2 - 4 * a * c)) / 2 * a
    print("x1 = ", round(x1, 4), " x2 = ", round(x2, 4))
elif d == 0:
    print("i am here")
    x1 = -b / 2 * a
    x2 = x1
    print("x1 = ", round(x1, 4), " x2 = ", round(x2, 4))
else:
    print("Roots not exists on the set of real numbers")