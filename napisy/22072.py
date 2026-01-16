napis = input()

smao = ['A', 'E', 'I', 'O', 'U']
for char in napis:
    for sam in smao:
        if char == sam:
            print(sam, end='')