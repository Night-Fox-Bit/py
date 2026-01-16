napis = list(input())
ile = 0

for i in range(len(napis) - 2):
    if napis[i] == napis[i + 1] == napis[i + 2]:
        napis[i + 2] = '0' if napis[i + 2] == '1' else '1'
        ile += 1

print(ile)