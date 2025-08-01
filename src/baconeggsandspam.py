from collections import defaultdict


while True:
    n = int(input())
    if not n:
        break
    cnt = defaultdict(set)
    for _ in range(n):
        s = input().split()
        for c in s[1:]:
            cnt[c].add(s[0])
    for k in sorted(cnt.keys()):
        res = [k, *sorted(cnt[k])]
        print(*res)
    print()
