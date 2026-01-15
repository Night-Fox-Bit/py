num1, num2 = map(float, input().split())

if num1 > num2:
    print(">")
elif num1 < num2:
    print("<")
else:
    print("=")