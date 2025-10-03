s = input()
cnt = {}
for b in range(len(s)):
    for e in range(b, len(s)):
        c = s[b:e + 1]
        cnt[c] = cnt.get(c, 0) + 1
res = (f"{-v} {k}" for v, k in sorted((-v, k) for k, v in cnt.items()))
print(*res, sep="\n")
