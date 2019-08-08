#Скоротити дріб виду m / n або вказати що він є нескоротним.
x = int(input("Введите чеслитель x="))
y = int(input("Введите знаменатель y="))
def gcd(a: int, b: int) -> int:
	while b:
		a, b = b, a % b
	return abs(a)
m=gcd(x,y)
new_x=x/m
new_y=y/m
if new_x==x and new_y==y:
    print("Дробь несокращается")
else:
    print("Новая дробь - %.0f/%.0f" % (new_x,new_y))