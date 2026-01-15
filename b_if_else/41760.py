a, b, c = map(float, input().split())

result = (a + b) / c

if result >= 1 and result.is_integer() == 0:
    print(f"{int(result)} {int(a + b - int(result) * c)}/{int(c)}")
elif result.is_integer():
    print(int(result))
else:
    print(f"{int(a + b)}/{int(c)}")