b, b_r, b_s, a, a_s = (int(i) for i in input().split())
# (b_r - b) * b_s < (res - a) * a_s
res = ((b_r - b) * b_s + a_s) // a_s + a
print(res)
