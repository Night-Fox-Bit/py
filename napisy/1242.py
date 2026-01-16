N = int(input())

napis = ""
for i in range(N):
    napis += input()

litery = sorted(set(napis), key=lambda x: (x.isupper(), x))

for litera in litery:
    if litera.isalpha():
        print(litera, napis.count(litera))
