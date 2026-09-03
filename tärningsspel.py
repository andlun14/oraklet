import random
import time

# | 7| 2, 4, 6, 9, 11| 3, 5, 8, 10, 12|

spelare_bank = 1000
dator_bank = 1000
spelare_bet = 0
dator_bet = 0
valt_fält = 0
tärning = 0
current_symbol = 0
landat_fält = 0
antal_rundor = 0

def clear():
    print("\033[H\033[J", end="")

def kolla_fält(tärning):
    if tärning == 7:
        return 1
    elif tärning in [2 or 4 or 6 or 9 or 11]:
        return 2
    else:
        return 3

def kolla_balans(balans):
    if balans <= 0:
        return True
    else:
        return False

def kolla_efter_vinnst(balans):
    if balans >= 10000:
        return True
    else:
        return False

def symbol_animation(num):
    current_symbol = 1
    time.sleep(1)
    while current_symbol < num:
        clear()
        current_symbol += 1
        if current_symbol == 2:
            print("| 7|*2, 4, 6, 9, 11| 3, 5, 8, 10, 12|")
        elif current_symbol == 3:
            print("| 7| 2, 4, 6, 9, 11|*3, 5, 8, 10, 12|")
        elif current_symbol == 4:
            print("| 7| 2,*4, 6, 9, 11| 3, 5, 8, 10, 12|")
        elif current_symbol == 5:
            print("| 7| 2, 4, 6, 9, 11| 3,*5, 8, 10, 12|")
        elif current_symbol == 6:
            print("| 7| 2, 4,*6, 9, 11| 3, 5, 8, 10, 12|")
        elif current_symbol == 7:
            print("|*7| 2, 4, 6, 9, 11| 3, 5, 8, 10, 12|")
            time.sleep(random.randint(10, 30) / 100)
        elif current_symbol == 8:
            print("| 7| 2, 4, 6, 9, 11| 3, 5,*8, 10, 12|")
        elif current_symbol == 9:
            print("| 7| 2, 4, 6,*9, 11| 3, 5, 8, 10, 12|")
        elif current_symbol == 10:
            print("| 7| 2, 4, 6, 9, 11| 3, 5, 8,*10, 12|")
        elif current_symbol == 11:
            print("| 7| 2, 4, 6, 9,*11| 3, 5, 8, 10, 12|")
        else:
            print("| 7| 2, 4, 6, 9, 11| 3, 5, 8, 10,*12|")
        time.sleep(random.randint(20, 40) / 100)

def spelares_tur():
    valt_fält = int(input("Fält 1, 2, eller 3?: "))
    spelare_bet = int(input("Hur mycket vill du satsa?: "))

    tärning = random.randint(2, 12)
    symbol_animation(tärning)
    time.sleep(2)
    landat_fält = kolla_fält(tärning)
    print(f"Det slogs {tärning} (fält {landat_fält}).")

    if valt_fält == landat_fält:
        return True, landat_fält, spelare_bet
    else:
        return False, landat_fält, spelare_bet

def dators_tur():
    time.sleep(1)
    valt_fält = random.randint(1, 3)
    print(f"Fält valt: {valt_fält}")
    time.sleep(1)
    dator_bet = random.randint(dator_bank / 10, dator_bank / 2)
    if (dator_bank - dator_bet) < 0:
        dator_bet = dator_bank
    print(f"Satsade pengar: {dator_bet}")
    time.sleep(1)

    tärning = random.randint(2, 12)
    symbol_animation(tärning)
    time.sleep(2)
    landat_fält = kolla_fält(tärning)
    print(f"Det slogs {tärning} (fält {landat_fält}).")

    if valt_fält == landat_fält:
        return True, landat_fält, dator_bet
    else:
        return False, landat_fält, dator_bet

print("Välkommen till roulette mot en slumpmässig dator. Spelet går ut på att antingen få 10 000 i banken eller att överleva tills datorn förlorar allt i banken. Det finns tre fält. Om du slår vad på fält ett som bara är nummer 7 och vinner så får du fem gånger sattsningen jämfört med två gånger om du satsar på någon av de andra fälten")

time.sleep(5)

while True:
    antal_rundor += 1
    print(f"Balans spelare: {spelare_bank}")
    print(f"Balans dator: {dator_bank}")

    time.sleep(2)

    print("Spelares tur.")
    vinnst_el_förloring, landat_fält, spelare_bet = spelares_tur()

    if vinnst_el_förloring == True:
        if valt_fält == 1:
            vinnst = spelare_bet * 5
        else:
            vinnst = spelare_bet * 2
        print(f"Du vann: {vinnst}")
        spelare_bank += vinnst
    else:
        print(f"Du förlorade: {spelare_bet}")
        spelare_bank = spelare_bank - spelare_bet

    if kolla_balans(spelare_bank):
        clear()
        print(f"Du förlorade på {antal_rundor} rundor.")   
        break 

    if kolla_efter_vinnst(spelare_bank):
        clear()
        print(f"Du vann på {antal_rundor} rundor.")
        break

    print("Datorns tur.")
    vinnst_el_förloring, landat_fält, dator_bet = dators_tur()

    if vinnst_el_förloring == True:
        if valt_fält == 1:
            vinnst = dator_bet * 5
        else:
            vinnst = dator_bet * 2
        print(f"Datorn vann: {vinnst}")
        dator_bank += vinnst
    else:
        print(f"Datorn förlorade: {dator_bet}")
        dator_bank = dator_bank - dator_bet

    if kolla_balans(dator_bank):
        clear()
        print(f"Datorn förlorade. Du vann på {antal_rundor} rundor.")
        break

    if kolla_efter_vinnst(dator_bank):
        clear()
        print(f"Datorn vann på {antal_rundor} rundor.")
        break

    time.sleep(4)
    clear()