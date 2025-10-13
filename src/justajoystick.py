n = int(input())
a, b = (input() for _ in range(2))
res = sum(min(abs(ord(ai) - ord(bi)), 26 - abs(ord(ai) - ord(bi))) for ai, bi in zip(a, b))
print(res)
