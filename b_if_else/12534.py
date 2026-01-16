a, b = map(float, input().split())

if a == 0:
    if b == 0:
        print("nieskonczenie wiele")
    else:
        print("brak")
else:
    x = -b / a
    print(x)