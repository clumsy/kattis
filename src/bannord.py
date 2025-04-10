s, m = (input() for _ in range(2))
res = " ".join("*" * len(c) if any(f in c for f in s) else c for c in m.split())
print(res)
