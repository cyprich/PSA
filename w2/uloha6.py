#!/usr/bin/env python3

# Budeme konštruovať takúto postupnosť celých čísel:
# - začneme zadaným číslom n
# - ak je párne, vydelíme ho 2
# - inak sa vynásobí 3 a pripočíta 1
# - toto sa opakuje, kým nedostaneme číslo 1
# Napíš program, ktorý pre dané štartové číslo vypíše takto skonštruovanú postupnosť

from typing import List


n: int = int(input("zadaj cislo: "))
zoznam: List[int] = [n]

while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n *= 3
        n += 1

    zoznam.append(n)

print(zoznam)
