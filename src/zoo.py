from collections import Counter


i = 0
while True:
    n = int(input())
    if not n:
        break
    i += 1
    cnt = Counter(input().split()[-1].lower() for _ in range(n))
    res = (f"{n} | {cnt[n]}" for n in sorted(cnt.keys()))
    print(f"List {i}:")
    print(*res, sep="\n")
