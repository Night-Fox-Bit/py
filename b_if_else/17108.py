x = float(input())

if x == 0 or x < -4:
    print(f"Wartosc wyrazenia dla {int(x) if x.is_integer() else x} nie istnieje!")
else:
    result = (x + 4) ** 0.5 / x
    if result.is_integer():
        print(int(result))
    else:
        print(result)
