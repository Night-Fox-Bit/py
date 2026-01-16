f_begin, f_end = map(int, input().split())
s_begin, s_end = map(int, input().split())

begin_max = max(f_begin, s_begin)
end_min = min(f_end, s_end)

if begin_max > end_min:
    print("null")
else:
    print(begin_max, end_min)