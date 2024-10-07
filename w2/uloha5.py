#!/usr/bin/env python3

# Budeme simulovať hádzanie viacerými hracími kockami. Napíš program ktorý si najprv vypýta n (počet hádzaní) a počet kociek. Potom vypíše čísla na kockách a ich súčet.
import random
from typing import List

n: int = int(input("zadaj pocet hadzani: "))
pocet_kociek: int = int(input("zadaj pocet kociek: "))

for i in range(n):
    zoznam: List[int] = []

    print("\n-------------------------------------\n")
    
    for j in range(1, pocet_kociek + 1):
        cislo: int = random.randint(1, 6)
        zoznam.append(cislo)
        print(f"na {j}. kocke padla {cislo}")
     
    print(f"ich sucet je {sum(zoznam)}")


