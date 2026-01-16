import math

a, b, c = map(float, input().split())

if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2
    pole = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(pole)
else:
    print(-1)