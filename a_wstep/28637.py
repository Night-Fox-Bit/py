n, sr_n, k, sr_k = map(float, input().split())

value_n = n * sr_n
value_k = k * sr_k

avg = (value_n + value_k) / (n + k)

print(avg)