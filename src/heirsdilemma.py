from itertools import permutations


def check(p):
    cur = "".join(str(i) for i in p)
    p = int(cur)
    if l <= p <= h and all(p % int(c) == 0 for c in cur):
        return 1
    return 0
l, h = (int(i) for i in input().split())
res = sum(check(p) for p in permutations(range(1, 10), 6))
print(res)
