a, b, c = map(int, input().split())

if a == 0:
    print("brak")
else:
    delt = b ** 2 - 4 * a * c
    if delt < 0:
        print("brak")
    elif delt == 0:
        x0 = -b / (2 * a)
        print(x0)
    else:
        x1 = (-b - delt ** 0.5) / (2 * a)
        x2 = (-b + delt ** 0.5) / (2 * a)
        print(*sorted([x1, x2]))
