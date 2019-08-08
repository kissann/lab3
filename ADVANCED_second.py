#Обчислити факторіал числа.
import math
while True:
    n = input("Введите число, для выхода нажмите ^: ")
    if n=='^':
        break
    else:
        n=int(n)
        print (math.factorial(n))