num = list(map(int, input().split()))

seven = 0
sodd = 0

for i in range(len(num)):
    if num[i] % 2:
        sodd += num[i]
    else:
        seven += num[i]

result = seven - sodd

print(result)