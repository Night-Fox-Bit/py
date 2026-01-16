a, b = map(int, input().split())

if a == 0 and b != 0:
    print(f"f(x)={b}")
elif a != 0 and b != 0:
    print(f"f(x)={a}x" if a != 1 and a != -1 else "f(x)=x" if a == 1 else "f(x)=-x", b if b < 0 else f"+{b}", sep="")
elif a == 0 and b == 0:
    print("f(x)=0")
else:
    print(f"f(x)={a}x" if a != 1 and a != -1 else "f(x)=x" if a == 1 else "f(x)=-x")
