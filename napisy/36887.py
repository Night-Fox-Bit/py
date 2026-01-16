napis = input()

ile_a = 0
for char in napis.lower():
    if char == 'a':
        ile_a += 1

if ile_a - len(napis) / 2 > 0:
    print("tak")
else:
    print("nie")