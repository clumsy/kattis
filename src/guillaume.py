n, s = int(input()), input()
res = [0, 0]
prv_d = cur_d = prv = cur = drw = 0
for i in reversed(range(n)):
    cur += s[i] == "G"
    drw += s[i] == "D"
    cur_d = n - i - drw
    if cur_d and (prv_d == 0 or cur * prv_d > prv * cur_d):
        res = [cur, cur_d - cur]
        prv, prv_d = cur, cur_d
res = "-".join(str(i) for i in res)
print(res)
