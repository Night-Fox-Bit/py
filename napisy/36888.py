napis = input()

szyfrowany = ""
for char in napis:
    if char.isupper():
        szyfrowany += '1'
    elif char.islower():
        szyfrowany += '0'
    else:
        szyfrowany += ' '

print(szyfrowany)