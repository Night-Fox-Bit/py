num = list(map(int, input().split()))

even = []
odd = []

for i in range(len(num)):
    if num[i] % 2:
        odd.append(num[i])
    else:
        even.append(num[i])

if len(even) > len(odd):
    print(odd[0])
else:
    print(even[0])