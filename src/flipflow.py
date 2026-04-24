t, s, n = (int(i) for i in input().split())
a = (int(i) for i in input().split())
p_t = c_s = 0
for i in a:
    c_s = s - max(0, c_s - (i - p_t))
    p_t = i
res = max(0, p_t + c_s - t)
print(res)
