from itertools import permutations


s = input()
res = None
for p in permutations(s):
    p = "".join(p)
    if p <= s:
        continue
    if res is None or p < res:
        res = p
res = res or 0
print(res)
