import math

d, n, m = map(int, input().split())

n_move = math.ceil(d / n)
m_move = math.ceil(d / m)

if n_move <= m_move:
    print("Jasiu")
else:
    print("Stasiu")