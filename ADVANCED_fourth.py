#Реалізуйте серію ігор “Камінь, ножиці, папір” із комп’ютером. У фіналі виведіть статистику виграшів людини та машини.
import random
Nich=0
Comp=0
Pl=0
l = ['0','1','2']
global n
def game(x,y):
    global Nich,Comp,Pl
    if x == y:
        print('Ничья')
        Nich += 1
    elif (x == '0' and y == '1') or (x == '1' and y == '2') or (x == '2' and y == '0'):
        print('Выигрыш')
        Pl += 1
    else:
        print('Проиграл')
        Comp += 1
    return Comp, Pl, Nich
n = int(input('Введите количество игр n '))
while n != 0:
    while True:
        x = input('Введите Камень (0), Ножницы (1), Бумага (2):')
        if x not in l:
            print('Введите 0, 1, 2')
        else: break
    y = random.choice(l)
    print("Компьютер выбрал: {0}\n".format(y))
    game(x, y)
    n -= 1
else:
    print('Победы - {0}\nПроигрыши - {1}\nНичьи- {2}'.format(Pl, Comp, Nich))