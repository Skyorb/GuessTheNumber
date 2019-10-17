#!usr/bin/env python3

from random import randint

tries = 0
number = randint (1, 100)

print("Rate zwischen 1 und 100!")
while True:
    try:
        guess = int(input(f'Versuch #{tries+1}:'))
        tries += 1
        if guess < number:
            print("Zahl ist zu klein, du Volltrottel.")
        elif guess > number:
            print("Zahl ist groß, du Idiot!")
        else:
            print(f"Richtig, das war Spitze! du hast die Zahl {number} nur {tries} Versuche gebraucht!")
            break
    except ValueError:
        print("Ungültige Eingabe!")
