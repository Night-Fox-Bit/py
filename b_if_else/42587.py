num=sorted(map(int,input().split()),reverse=True)

if str(num[0])+str(num[1]) >= str(num[1])+str(num[0]):
    print(f"{num[0]}{num[1]}")
else:
    print(f"{num[1]}{num[0]}")
