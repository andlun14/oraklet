import random

svar = ["Ja, helt klart.", "Absolut inte.", "Fråga igen imorgon.", "Det vill du inte veta.", "Kanske...", "Absolut!", "Nej, inte en bra idé."]

fråga = input("fråga oraklet: ")
print("Du frågade: ", fråga)
print(random.choice(svar))
