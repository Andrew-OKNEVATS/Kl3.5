import random #Додаємо бібліотеку щоб була можливість функції випадковості


class stats: #створюємо класс з класичними характеристиками
    def __init__(self):
        self.hp = 100
        self.money = 50
        self.attack = 2

your_hero = stats() #зміна для звичайного героя

your_hero2 = stats() #зміна для випадкового героя
your_hero2.hp = random.randint(50,150) #змінюємо значення, робимо відміність від класичних характеристик,життя
your_hero2.money = random.randint(20,70) #змінюємо значення, робимо відміність від класичних характерисик,монети


star = input("Вибір героя звичаний (Y), видковий (N)")

if star == "Y":
    print("Ви обрали звичайного героя")
    print("Життя:",your_hero.hp, "Монети:",your_hero.money, "Атака:",your_hero.attack)
    your_hero2 = your_hero

elif star == "N":
    print("Ви обрали випадкового героя")
    print("Життя:", your_hero2.hp, "Монети:", your_hero2.money, "Атака:", your_hero2.attack)
    your_hero = your_hero2

vubir = input("Магазин(N), Бос(B)")

if vubir == "N":
    vubir2 = input("Сапоги Гермеса:20(S), Вихід(B)")
    if vubir2 == "S":
        print("Дякую за покупку!")
        your_hero.hp +=20
        your_hero.money-=20
print("Життя:", your_hero.hp, "Монети:", your_hero.money, "Атака:", your_hero.attack)


if vubir == "B":
    print("Error 404")
