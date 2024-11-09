import random #Додаємо бібліотеку щоб була можливість функції випадковості
from asyncio import wait_for
import time

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
vubir = input("Магазин(N), Бос(B), Тренування(T), Банк(K)")
if vubir == "N":
    vubir2 = input("Сапоги Гермеса:20(S), Вихід(B)")
    if vubir2 == "S":
        print("Дякую за покупку!")
        your_hero.hp +=20
        your_hero.money-=20
print("Життя:", your_hero.hp, "Монети:", your_hero.money, "Атака:", your_hero.attack)
if vubir == "B":
    print("Error 404")
if vubir == "T":
    vubir3 = input("Безкоштовне тренування-0 монет(B),економ тренування-10 монет(E),елітне тренування-20 монет(V)")
    if vubir3 == "B":
        print("Почекайте 60 секунд")
        time_limit = 60
        start_time = time.time()
        while True:
            elapsed_time = time.time() - start_time
            print(time_limit- int(elapsed_time))
            if elapsed_time > time_limit:
                print("Тренування Закінчено +1 атака")
                your_hero.attack +=1
                break
    elif vubir3 == "E":
        print("Почекайте 25 секунд")
        time_limit = 25
        start_time = time.time()
        while True:
            elapsed_time = time.time() - start_time
            print(time_limit- int(elapsed_time))
            if elapsed_time > time_limit:
                print("Тренування Закінчено +3 атаки")
                your_hero.attack +=3
                your_hero.money -=10
                break
    elif vubir3 == "V":
        print("Почекайте 5 секунд")
        time_limit = 5
        start_time = time.time()
        while True:
            elapsed_time = time.time() - start_time
            print(time_limit- int(elapsed_time))
            if elapsed_time > time_limit:
                print("Тренування Закінчено +5 атаки")
                your_hero.attack +=5
                your_hero.money -=20
                break
if vubir == "K":
    print("Купити Банк?(35 монет)")
    vubir4 = input("Так(Y),Ні(N)")
    if vubir4 == "Y":
        print("Ви купили банк тепер кожні 5 секунд вам буде приходити 2 монети")
        while True:
            time_limit = 5
            start_time = time.time()
            bank_time = time.time() - start_time
            time_limit- int(bank_time)
            if bank_time > time_limit:
                your_hero.money +=2
    your_hero.money -=35
    vubir5 = input("Магазин(M),Бос(B),Тренування(T),Банк(K)")
    if vubir5 == "K":
        print("Монети",your_hero.money)
