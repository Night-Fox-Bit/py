zdanie = input()

n_napis = ""
for wyraz in zdanie.split():
    if len(wyraz) > 0:
        n_napis += wyraz[0].upper() + wyraz[1:]
    n_napis += " "

print(n_napis)