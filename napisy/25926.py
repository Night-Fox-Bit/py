n = int(input())

result = 0
for i in range(n):
    napis = input()
    if napis[len(napis) - 1] == '0':
        result += 1

print(result)