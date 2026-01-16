n = int(input())

for i in range(n):
    napis = input()
    if len(napis) >= 5 and napis[0] == napis[len(napis) - 1]:
        print(napis)