napis = input()

if napis[len(napis) -1].islower():
    print(napis.upper())
else:
    print(napis.lower())