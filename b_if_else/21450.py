n, t, p = map(int, input().split())

v1 = p / t
v2 = (n - p) / t

print(*sorted([v1, v2]))