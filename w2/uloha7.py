#!/usr/bin/env python3

# Napíš funkciu obdlznik(sirka, znak='*'), ktorá z daného znaku znak vypíše do troch riadkov výstupu obdĺžnik zadanej šírky.

def obdlznik(sirka: int, znak: str = "*") -> None:
    print(f"{znak*sirka}\n{znak}{' ' * (sirka - 2)}{znak}\n{znak*sirka}")

obdlznik(30, "#")
obdlznik(6)
obdlznik(19, "O")
