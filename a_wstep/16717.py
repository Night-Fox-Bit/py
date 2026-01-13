num = list(map(int, input().split()))
size = len(num)

result=0
pows = [0] * size
for i in range(size):
    pows[i] = pow(2, i)
    result += num[size - 1 - i] * pows[i]

print(result)