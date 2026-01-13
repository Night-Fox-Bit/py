num = int(input())
result = 0

if num>0:
    result += num % 10

if num >= 10:
    result += num // 10 % 10

if num >= 100:
    result += num // 100 % 10

if num >= 1000:
    result += num // 1000

print(result)
