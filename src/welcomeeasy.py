n = int(input())
for k in range(n):
    s = input()
    tgt = "welcome to code jam"
    cnt = {tgt[:i]: 0 if i else 1 for i in range(len(tgt) + 1)}
    for c in s:
        for i in range(len(tgt), 0, -1):
            prefix = tgt[:i]
            if prefix[-1] == c:
                cnt[prefix] += cnt[prefix[:-1]]
    res = f"Case #{k + 1}: {cnt[tgt]:04d}"
    print(res)
