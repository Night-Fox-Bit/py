pot = [27, 9, 3, 1]
num = list(map(int, input().split()))
result = 0
for i in range(4):
    result+=pot[i] * num[i]
print(result)