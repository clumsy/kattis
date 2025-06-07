r, g, b = (int(i) for i in input().split())
res = (
    "svartur" if r == b == g == 0 else
    "hvitur" if r == b == g == 255 else
    "raudur" if r > max(g, b) else
    "graenn" if g > max(r, b) else
    "blar" if b > max(g, r) else
    "gulur" if r == g and b < r else
    "fjolubleikur" if r == b and g < r else
    "blagraenn" if g == b and r < g else
    "grar" if r == g == b and 0 < b < 255 else
    "othekkt"
)
print(res)
