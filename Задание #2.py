kol = int(input("Введите количество билетов \n"))
age = [int(input("Введите возраст посетителя \n")) for i in range(1,kol+1)]
s = 0 #переменная-счетчик, в которой считаем стоимость
for i in age:
    if i < 18:
        price = 0
        s = s + price
    elif 18 <= i < 25:
        price = 990
        s = s + price
    else:
        price = 1390
        s = s + price
if kol >= 3:
    print(s*0.9)
else:
    print(s)









