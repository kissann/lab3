#Згенерувати 10 серій із 0, 1 та 2 таких, що сума чисел була рівна 12
import random
n=0
#while n!=0:
sum=0
while n!=10:
    while sum!=12:
        y = random.randint(0,2)
        print(y)
        sum=int(sum)+int(y)
        if 12-int(sum)<2:
            y = 1
            print(y)
            sum = int(sum) + int(y)
        elif 12 - sum < 3:
            y = 2
            print(y)
            sum = int(sum) + int(y)
    print("Сумма =  %.0f\n" %sum)
    sum=0
    n+=1
