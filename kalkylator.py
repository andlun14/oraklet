print("Det här är en kalkylator. Skriv nedan de två nummerna du vill arbeta med samt vad du vill göra med dem.")

while True:
    nummer_1 = float(input("Nummer 1: "))
    nummer_2 = float(input("Nummer 2: "))
    symbol = input("Vad vill du göra med nummerna(+ , - , * , /)?: ")

    if symbol == "+":
        svar = nummer_1 + nummer_2
    elif symbol == "-":
        svar = nummer_1 - nummer_2
    elif symbol == "*":
        svar = nummer_1 * nummer_2
    elif symbol == "/":
        svar = nummer_1 / nummer_2
    else:
        print("Fel symbol eller annat fel.")

    if (svar).is_integer():
        svar = int(svar)

    print(f"Svaret blev: {svar}.")
    Break = input("Fortsätt räkna(Y/N)?")
    if Break != "Y":
        break