s = [input() for _ in range(5)]
res = [str(i + 1) for i, c in enumerate(s) if "FBI" in c] or ["HE GOT AWAY!"]
res = " ".join(res)
print(res)
