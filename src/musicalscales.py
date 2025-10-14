n = int(input())
ns = input().split()
ns = set(ns)
ss = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
nss = len(ss)
res = []
for i, s in enumerate(ss):
    scale = {
        s,
        ss[(i + 2) % nss],
        ss[(i + 4) % nss],
        ss[(i + 5) % nss],
        ss[(i + 7) % nss],
        ss[(i + 9) % nss],
        ss[(i + 11) % nss],
        ss[(i + 12) % nss],
    }
    if scale & ns == ns:
        res.append(s)
res = res or ["none"]
print(*res)
