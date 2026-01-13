num = float(input())

integer = int(num)
decimal = int(num * 100) % 100

print(integer, f"0.{decimal}")