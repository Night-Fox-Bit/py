str1 = input()

str2 = ""
for i in range(len(str1)):
    if i % 2 == 0:
        str2 += str1[i].upper()
    else:
        str2 += str1[i]

print(str2)