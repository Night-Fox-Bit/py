n = int(input())

for i in range(n):
    a, b = input().split()
    if len(a) > len(b):
        print(a)
    elif len(b) > len(a):
        print(b)
    else:
        if a[0] < b[0]:
            print(a)
        elif b[0] < a[0]:
            print(b)
        else:
            print(a, b)