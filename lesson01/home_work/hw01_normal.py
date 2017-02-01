import math
# Задача-1: Дано произвольное целое число, вывести самую большую цифру
# этого числа
NUMBER = 123865748021
RESULT = 0
while NUMBER:
    NUMBER = NUMBER // 10
    RESULT = NUMBER % 10 if RESULT < NUMBER % 10 else RESULT
print(RESULT)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу используя только две переменные
NUMBER_A = float(input("numberA = "))
NUMBER_B = float(input("numberB = "))
NUMBER_A = NUMBER_A + NUMBER_B
NUMBER_B = NUMBER_B - NUMBER_A
NUMBER_B = -NUMBER_B
NUMBER_A = NUMBER_A - NUMBER_B
print("a = ", NUMBER_A, "b = ", NUMBER_B)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида ax2 + bx + c = 0.
# Для вычисления квадратного корня воспользуйтесь функицй sqrt() молудя math
# import math
# math.sqrt(4) - вычисляет корень числа 4
print("** Hi, I am a program that can help you with \"quadratic equation\" like (ax2 + bx + c = 0)")
A = float(input("a = "))
B = float(input("b = "))
C = float(input("c = "))
D = B**2 - 4 * A * C
X1 = 0
X2 = 0
print("Discriminant = ", D)
if D > 0:
    X1 = (-B + math.sqrt(B**2 - 4 * A * C)) / 2 * A
    X2 = (-B - math.sqrt(B**2 - 4 * A * C)) / 2 * A
    print("x1 = ", round(X1, 4), " x2 = ", round(X2, 4))
elif D == 0:
    X1 = -B / 2 * A
    X2 = X1
    print("x1 = ", round(X1, 4), " x2 = ", round(X2, 4))
else:
    print("Roots not exists on the set of real numbers")
