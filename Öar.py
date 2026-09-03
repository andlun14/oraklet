a, b = 0, 1
x = 0
antal_deltagare = int(input("Hur många deltagare är med?(>1 och <10000):"))
n = antal_deltagare

while n > 0:
    a, b = b, a + b
    n = n - a
    x += 1

print(f"Den {antal_deltagare}:te deltagaren försvann på ö nummer {x}")