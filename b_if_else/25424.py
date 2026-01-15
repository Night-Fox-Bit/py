a, b, c = map(float, input().split())

if a == b == c:
    print(3)
elif a == b or a == c or b == c:
    print(2)
else:
    print(1)
