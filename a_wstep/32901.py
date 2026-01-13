znak, num1, num2 = map(str, input().split())

num1 = int(num1)
num2 = float(num2)

result = int(ord(znak) + num1 + num2)

print(result)