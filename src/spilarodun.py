n = int(input())
ts = []
for t in ["Venjulegt", "Ahrifa", "Bodunar", "Samruna", "Samstillt", "Thaeo", "Penduls", "Tengis"]:
    ts.append(f"Skrimsli - {t}")
for t in ["Venjulegur", "Bunadar", "Svida", "Samfelldur", "Bodunar", "Hradur"]:
    ts.append(f"Galdur - {t}")
for t in ["Venjuleg", "Samfelld", "Mot"]:
    ts.append(f"Gildra - {t}")
ts.append("Annad")
ts = {n: i for i, n in enumerate(ts)}


def parse(s):
    n, i, t, d = s.split(",")
    return {"nafn": n.strip(), "id": i.strip(), "flokkur": ts[t.strip()], "dagsetning": d.strip()}


def order(s):
    return lambda x: tuple(x[c] for c in s)


s = [parse(input()) for _ in range(n)]
s = sorted(s, key=order(input().split()))
res = [e["nafn"] for e in s]
print(*res, sep="\n")
