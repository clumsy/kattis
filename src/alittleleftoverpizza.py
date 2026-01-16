n = int(input())
cnt = [0] * 3
for _ in range(n):
    t, c = input().split()
    cnt[0 if t == "S" else 1 if t == "M" else 2] += int(c)
res = (cnt[0] + 5) // 6 + (cnt[1] + 7) // 8 + (cnt[2] + 11) // 12
print(res)
