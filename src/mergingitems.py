k = int(input())
cnt = [0] * 60
for _ in range(k):
    cnt[int(input())] += 1
n = int(input())
cnt[0] += 3 * n
res = []
for i in range(1, len(cnt)):
    cnt[i] += cnt[i - 1] // 2
    cnt[i - 1] %= 2
    if cnt[i - 1]:
        res.append(i - 1)
print(*res)
