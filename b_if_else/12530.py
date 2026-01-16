chars = list(input().split())

for i in chars:
    if i.islower():
        print("m", end=" ")
    elif i.isupper():
        print("d", end=" ")
    elif i.isdigit():
        print("c", end=" ")
    else:
        print("i", end=" ")