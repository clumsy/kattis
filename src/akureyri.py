from collections import Counter


n = int(input())
cnt = Counter()
for _ in range(n):
    input()
    s = input()
    cnt[s] += 1
for k, c in cnt.items():
    print(k, c)
