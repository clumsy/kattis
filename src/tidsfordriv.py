n = int(input())
vs = "A,2,3,4,5,6,7,8,9,10,J,Q,K".split(",")
cnt = dict(zip(vs, [4] * len(vs)))
for _ in range(n):
    c = input()
    cnt[c[:-1]] -= 1
res = max(cnt.values()) / (52 - n)
print(res)
