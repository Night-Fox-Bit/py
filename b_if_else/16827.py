x = float(input())

if x < 1 or x >= 10:
    print("brak")
else:
    result = (x - 1) ** 0.5 / (10 - x) ** 0.5
    print(result)