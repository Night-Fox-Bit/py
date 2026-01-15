num = sorted(list(map(float, input().split())), reverse=True)

result = num[0] - num[len(num) - 1]

if result.is_integer():
    print(int(result))
else:
    print(result)