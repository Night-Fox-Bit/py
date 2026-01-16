n = int(input())

for i in range(n):
    napis = input()
    tnapis = []
    for char in napis:
        tnapis.append(char)
    if sorted(tnapis)[0] == '1':
        print(napis)