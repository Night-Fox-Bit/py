#python ma problem z tym zadaniem
a, b, c = map(float, input().split())

if a == 0 or b == 0 or c == 0:
    print("error")
else:
    if 1 / a + 1 / b + 1 / c == 0:
        print("error")
    else:
        result = 3 / (1 / a + 1 / b + 1 / c)
        print(result)
