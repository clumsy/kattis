t = int(input())
for _ in range(t):
    s = input()
    res = 0
    for i, c in enumerate(s[::-1]):
        c = int(c)
        if i & 1 == 1:
            c = sum(divmod(int(c) * 2, 10))
        res += c
    res = "PASS" if res % 10 == 0 else "FAIL"
    print(res)
