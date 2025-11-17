n, m = (int(i) for i in input().split())
ts = sorted(int(i) for i in input().split())
ls = sorted(int(i) for i in input().split())
res = 0
while ts and ls:
    if ts[-1] <= ls[-1]:
        res += 1
        ls.pop()
    ts.pop()
print(res)
