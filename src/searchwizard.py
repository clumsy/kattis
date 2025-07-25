w, m = input(), int(input())
s = input()
full = w + "#" + s
p = [0] * len(full)
res = k = 0
for i in range(1, len(full)):
    while k and full[i] != full[k]:
        k = p[k - 1]
    k += full[i] == full[k]
    p[i] = k
    res += len(w) == p[i]
print(res)
