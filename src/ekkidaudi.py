a, b = (input().split("|") for _ in range(2))
res = " ".join(ai + bi for ai, bi in zip(a, b))
print(res)
