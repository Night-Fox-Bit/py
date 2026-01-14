num1, num2, num3 = map(float, input().split())

if num1 > num2 > num3:
    print("malejacy")
elif num1 < num2 < num3:
    print("rosnacy")
else:
    print("niemonotoniczny")