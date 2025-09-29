t = int(input())
for _ in range(t):
    n = list(input())
    for i in reversed(range(len(n))):
        if n[i] != "0":
            n[i] = str(int(n[i]) - 1)
            break
    res = "".join(n).lstrip("0") or 0
    print(res)
