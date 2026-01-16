t = int(input())

for i in range(t):
    napis = input()
    if (len(napis) / 2).is_integer():
        print(napis[:int(len(napis) / 2)])
    else:
        print(napis[:int(len(napis) / 2) + 1])