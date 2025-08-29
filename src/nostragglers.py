n = int(input())
cnt = {}
for _ in range(n):
    s = input().split()
    cnt[s[0]] = cnt.get(s[0], 0) + (1 if s[1] == "IN" else -1) * int(s[2])
res = sum(cnt.values()) or "NO STRAGGLERS"
print(res)
