#Перевірити чи є вказаний рік високосний.
year=int(input("Введите год:"))
if year % 4!=0:
    print("Год %.0f не высокосный " % year)
elif year % 100 == 0:
    if year % 400 == 0:
        print("Год %.0f высокосный"  % year)
    else:
        print("Год %.0f не высокосный " % year)
else:
    print("Год %.0f высокосный"  % year)
