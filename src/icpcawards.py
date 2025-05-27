n = int(input())
seen = set()
for _ in range(n):
    u, t = input().split()
    if u not in seen and len(seen) < 12:
        print(u, t)
        seen.add(u)
