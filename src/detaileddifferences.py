n = int(input())
for _ in range(n):
    s1, s2 = (input() for _ in range(2))
    print(s1, s2, sep="\n")
    res = "".join("*" if c1 != c2 else "." for c1, c2 in zip(s1, s2))
    print(res)
    print()
