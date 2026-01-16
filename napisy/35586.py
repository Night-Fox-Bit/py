zdanie = input()

d_wyraz = []

for wyrazy in zdanie.split():
    d_wyraz.append(len(wyrazy))

print(*d_wyraz)