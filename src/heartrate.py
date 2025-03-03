n = int(input())
for _ in range(n):
    b, p = (float(i) for i in input().split())
    bpm, d = (60 * b) / p, 60 / p
    res = bpm - d, bpm, bpm + d
    print(*res)
