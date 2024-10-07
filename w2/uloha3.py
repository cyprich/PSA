#!/usr/bin/env python3

# Napíš program, ktorý zo znakov hviezdička ('*') vytvorí takýto trojuholník: v 1. riadku je jedna hviezdička, v 2. dve, v 3. tri, …, v n-tom riadku je n hviezdičiek

n: int = int(input("zadaj pocet riadkov: "))

for i in range(1, n + 1):
    print("*" * i)
