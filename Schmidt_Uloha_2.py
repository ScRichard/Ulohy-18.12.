import random

pokusy = 0

hadajuce = random.randint(0, 1000)

print("Myslím si číslo od 1 až do 1000, a ty ho budeš hádať!")

while True:
    a = 0
    try:
        a = int(input("Tvoj typ? "))
    except Exception as e:
        print("Skús znovu!")
        continue


    if a < hadajuce:
        print("Myslím na vačšie číslo!")
        pokusy += 1
    elif a > hadajuce:
        print("Myslím na menšie číslo!")
        pokusy+=1
    else:
        print(f"Gratulujem uhádli ste moje číslo na {pokusy} pokusov!")
        break
