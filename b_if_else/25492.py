num = list(map(int, input().split()))

even = 0

for i in range(len(num)):
    if num[i] % 2 == 0:
        even += 1

print(even)