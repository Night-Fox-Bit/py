import math
#b_if_else ale to math

a, b = map(float, input().split())

result = math.floor(b) - math.ceil(a) + 1

print(result)