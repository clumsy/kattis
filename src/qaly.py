n = int(input())
qy = ((float(f) for f in input().split()) for _ in range(n))
res = sum(q * y for q, y in qy)
print(res)
