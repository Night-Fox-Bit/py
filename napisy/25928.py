n = int(input())

for i in range(n):
    ile_1 = 0
    ile_0 = 0
    napis = input()
    for char in napis:
        if char == '1':
            ile_1 += 1
        elif char == '0':
            ile_0 +=1
    if ile_0 == ile_1:
        print(napis)