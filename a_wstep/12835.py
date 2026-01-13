time = int(input())

hour = time // 60
minute = time - hour * 60

print(f"{hour}h {minute}min")