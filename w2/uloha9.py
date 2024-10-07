#!/usr/bin/env python3

# Napíšte program, ktorý vypýta číslo n. Následne vygeneruje n celočíselných vektorov o dĺžke n a následne tieto vektory zoradí podľa 1. súradnice, 2., ... Až n-tej súradnice.

from typing import List
import random


n: int = int(input("zadaj cislo n: "))

zoznam: List[List[int]] = []


for i in range(n):
    vektor: List[int] = []
    
    for j in range(n):
        vektor.append(random.randint(1, 9))

    zoznam.append(vektor)

print(zoznam)
