t, d = map(float, input().split())

minuty = int(t // 1)
sekundy = int(t * 100 % 100)

tempo_sek = minuty * 60 + sekundy
czas_sek = int(tempo_sek * d)

h = czas_sek // 3600
m = (czas_sek % 3600) // 60
s = czas_sek % 60

print(f"{h}h {m}min {s}s")