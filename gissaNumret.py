import random

nummer = random.randint(1, 100)
print("Ett nummer mellan 1 och 100 har valts, du har fem försök på dig att gissa vad numret är...")
klarad = 0
i = 1
while i < 6:
    gissning = input("Skriv din gissning:")
    if gissning == nummer:
        print("Rätt!")
        klarad = 1
        break
    elif gissning < nummer:
        print("Större.")
    elif gissning > nummer:
        print("Mindre.")
    print(i, "försök kvar.")
if klarad == 0:
    print("Slut på försök...")