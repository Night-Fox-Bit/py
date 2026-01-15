num = sorted(list(map(float, input().split())), reverse=True)

result = num[0] + num[1] + num[2]

if result.is_integer():
    print(int(result))
else:
    print(result)