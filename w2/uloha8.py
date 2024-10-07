#!/usr/bin/env python3

# Napíš funkciu vyhod_medzery(text), ktorá zo zadaného textu vyhodí všetky medzery. Funkcia nič nevypisuje, ale pomocou return vráti nový reťazec. Otestuj ju s rôznymi hodnotami parametrov.

def vyhod_medzery(text: str) -> str:
    result = ""
    for i in text:
        if i != " ":
            result += i

    return result

print(vyhod_medzery(' mám rád Python '))

