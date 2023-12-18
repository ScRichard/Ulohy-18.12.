# Kocky
import random

class Kocky:
    def __init__(self):
        self.running = 1


    def startup(self):
        while self.running:
            try:
                self.run(int(input("Zadaj pocet kôl: ")))
            except Exception as e:
                print("Zlé zadané hodnoty, skús znovu!")

    def run(self, kola):
        player1 = 0
        player2 = 0
        for i in range(kola):

            num1 = [random.randint(1, 6), random.randint(1, 6)]
            num2 = [random.randint(1, 6), random.randint(1, 6)]
            s1 = sum(num1)
            s2 = sum(num2)
            print(f"Hrač č1: {num1} Súčet: {s1}")
            print(f"Hrač č2: {num2} Súčet: {s2}")
            print("--------------------")

            if s1 > s2:
                player1 +=1
            elif s1 < s2:
                player2 +=1

        print(f"Vysledok:  H1: {player1}   H2: {player2}")

        a = input("Želáte si hrať znovu? (y/n) ")

        if a != "y":
            self.running = False
            print("Ďakujem vám za hranie!")
