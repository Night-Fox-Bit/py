napis = input()

litery = list(napis[::2])
rlitery = list(napis[1::2])

rlitery.reverse()
odszyfrowany = ''.join(litery + rlitery)

print(odszyfrowany)