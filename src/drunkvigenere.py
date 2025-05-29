s, k = (input() for _ in range(2))
res = "".join(
    chr(ord("A") + (ord(si) - ord("A") + (-1 if i & 1 == 0 else 1) * (ord(ki) - ord("A"))) % 26)
    for i, (si, ki) in enumerate(zip(s, k))
)
print(res)
