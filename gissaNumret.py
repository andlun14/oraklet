import random

nummer = random.randint(1, 100)
print("Ett nummer mellan 1 och 100 har valts, du har tio försök på dig att gissa vad numret är...")
klarad = 0
i = 1
while i < 11:
    gissning = int(input("Skriv din gissning:"))
    if gissning == nummer:
        print("Rätt!")
        klarad = 1
        break
    elif gissning < nummer:
        print("Större.")
    elif gissning > nummer:
        print("Mindre.")
    print((10 - i), "försök kvar.")
    i += 1
if klarad == 0:
    print("Slut på försök...")
    print(f"Numret var: {nummer}")