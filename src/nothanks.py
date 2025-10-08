n, a = int(input()), (int(i) for i in input().split())
cnt = [False] * 90001
for i in a:
    cnt[i - 1] = True
res = 0
for i in range(len(cnt)):
    res += i + 1 if cnt[i] and (i == 0 or not cnt[i - 1]) else 0
print(res)
