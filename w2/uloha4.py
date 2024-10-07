#!/usr/bin/env python3

# Vo vlaku sa vezie 100 cestujúcich. V každej stanici, v ktorej zastane, niekoľko ľudí vystúpi a niekoľko nastúpi. Napíš program, ktorý odsimuluje n takýchto staníc s vystupovaním a nastupovaním cestujúcich. Predpokladáme, že v každej stanici vystúpi aj nastúpi náhodný počet cestujúcich z intervalu <0, 9>.
import random

n: int = int(input("zadaj pocet stanic: "))
cestujuci: int = 100

for i in range(n):
    plus: int = random.randint(0, 9)
    minus: int = random.randint(0, 9)
    novycestujuci: int = cestujuci + plus - minus
    print(f"vo vlaku bolo {cestujuci} cestujucich, {plus} nastupilo, {minus} vystupilo, {novycestujuci} zostalo")
    cestujuci = novycestujuci
