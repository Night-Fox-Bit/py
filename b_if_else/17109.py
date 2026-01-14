x = int(input())

if (pow(x, 2) - 6 * x + 5) >= 0 and x != 0:
    result = (pow(x, 2) - 6 * x + 5) ** 0.5 / x
    print(result)
else:
    print(f"Dla liczby {x} wartosc wyrazenia nie istnieje!")