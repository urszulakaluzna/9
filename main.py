import random

a = random.randrange(1, 9)
c = 5
while (c > 0):
    b = int(input("Zgadnij liczbę w zakresie 1-9.\n"))

    if b < a:
        print("Zbyt nisko, spróbuj jeszcze raz.")
        c -= 1
    elif b > a:
        print("Za wysoko, spróbuj jeszcze raz.")
        c -= 1
    elif a == b:
        print("Zgadłeś")
        break