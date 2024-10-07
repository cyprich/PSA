#!/usr/bin/env python3
# Napíš program, ktorý prečíta polomer kruhu a vypíše obvod a obsah tohto kruhu. Môžeš predpokladať, že pi = 3.14159

pi: float = 3.14159
r: float = float(input("zadaj polomer kruhu: "))

print(f"obvod kruhu = {2 * pi * r}")
print(f"obsah kruhu = {pi * r ** 2}")

