b = int(input())

if b == 0:
    print(1)
else:
    n = b % 4
    if n == 0:
        print(6)
    elif n == 1:
        print(2)
    elif n == 2:
        print(4)
    else:
        print(8)