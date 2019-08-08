#Написати простий калькулятор на чотири арифметичні дії.
print("Калькулятор. Для выхода из программы введите ^")
while True:
    x = input("x=")
    if x=='^':break
    zn = input("Введите знак (+,-,*,/): ")
    if zn == '^': break
    y = input("y=")
    if y=='^': break
    else:
        x=float(x)
        y=float(y)
        if zn == '+':
            print("%.2f" % (x + y))
        elif zn == '-':
            print("%.2f" % (x - y))
        elif zn == '*':
            print("%.2f" % (x * y))
        elif zn == '/':
            if y != 0:
                print("%.2f" % (x / y))
            else:
                print("На ноль делить нельзя!")
        else:
            print("Знак не понятен")




