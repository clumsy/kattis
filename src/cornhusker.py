a = (int(i) for i in input().split())
n, kwf = (int(i) for i in input().split())
s = [1] * 5
for i, e in enumerate(a):
    s[i // 2] *= e
res = ((sum(s) // 5) * n) // kwf
print(res)
