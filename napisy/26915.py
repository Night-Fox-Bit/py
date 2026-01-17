napisy = []

while True:
    napis = input()
    if napis == "KONIEC":
        break
    napisy.append(napis)

for n in reversed(napisy):
    print(n)