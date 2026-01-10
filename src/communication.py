n = int(input())
xs = (int(i) for i in input().split())


def solve(x):
    res = i = p = 0
    while i < 8:
        c = (x >> i) & 1
        res |= (c ^ p) << i
        p = c ^ p
        i += 1
    return res


res = (solve(i) for i in xs)
print(*res)
