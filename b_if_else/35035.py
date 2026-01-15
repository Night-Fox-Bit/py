num1, num2, num3 = map(float, input().split())

avg = (num1 + num2) / 2

if avg < num3:
    print("tak")
else:
    print("nie")