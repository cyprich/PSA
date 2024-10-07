#!/usr/bin/env python3

# V jednom starodávnom príbehu sa na políčka šachovnice kládli zrniečka ryže: na 1. políčko 1 zrnko ryže, na ďalšie 2, na každom ďalšom je dvojnásobok predchádzajúceho. Napíš program, ktorý vypíše, koľko zrniek bude na n-tom políčku.

n: int = int(input("zadaj cislo policka: "))

ryza: int = 1

for i in range(n - 1):
    ryza *= 2

print(f"na policku {n} bude {ryza} zrniecok ryze")
