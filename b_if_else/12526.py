year = int(input())

if (year / 4).is_integer() and (year / 100).is_integer() == 0 or (year / 400).is_integer():
    print("Tak")
else:
    print("Nie")