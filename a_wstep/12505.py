x1, y1, z1, x2, y2, z2 = map(int, input().split())

result = (pow(x1 - x2, 2) + pow(y1 - y2, 2) + pow(z1 - z2, 2)) ** 0.5

print(result)