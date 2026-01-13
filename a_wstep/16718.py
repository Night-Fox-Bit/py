pot = [27, 9, 3, 1]
num = list(map(int, input().split()))
sum = 0
for i in range(4):
    sum+=pot[i] * num[i]
print(sum)