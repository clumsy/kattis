w, h, d = (int(i) for i in input().split())
j, c = [0] * 2, [0] * 2
for r in range(h):
    s = input()
    ji = s.find("J")
    if ji >= 0:
        j = [r, ji]
    ci = s.find("@")
    if ci >= 0:
        c = [r, ci]
di, dj = j[0] - c[0], j[1] - c[1]
res = "no jumpscares here" if di * di + dj * dj > d * d else "the guide is right"
print(res)
