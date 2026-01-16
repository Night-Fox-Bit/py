n = int(input())

result = 0
for i in range(n):
    napis = input()
    if (len(napis) / 2).is_integer():
        result += 1

print(result)