
while True:

    c1 = 0
    c2 = 0
    try:
        c1 = int(input("Súčet dvoch čísel: "))
        c2 = int(input("Rozdiel dvoch čísel: "))
        if c1 < c2 or c1 < 0 or c2 < 0:
            print("Nevhodné parametre")
            continue
    except Exception as e:
        print("Nevhodné parametre")
        continue

    print(f"Tvoje čísla sú: {int((c1+c2)/2)} , {int(c1 - (c1+c2)/2)}")
