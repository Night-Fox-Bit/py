num = list(map(int, input().split()))

a = sum(num) / len(num)

product = 1
for i in range(len(num)):
    product*=num[i]

g = product ** (1/len(num))

if a > g:
    print("a")
elif a < g:
    print("g")
else:
    print("ga")