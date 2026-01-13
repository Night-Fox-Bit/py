num = list(map(int, input().split()))
result = num[0]%10 + num[1]//10 + num[2] ** 0.5
print(result)