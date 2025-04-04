n = int(input())
res, cache = None, {}
for _ in range(n):
    s = input().split()
    cache[s[0]] = cache.get(s[0], 0) + int(s[1])
    if not res or cache[s[0]] > cache[res]:
        res = s[0]
print(res)
