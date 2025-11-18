y, p = input().split()
res = (
    y + p
    if y.endswith("ex")
    else y + "x" + p
    if y[-1] == "e"
    else y[:-1] + "ex" + p
    if y[-1] in "aiou"
    else y + "ex" + p
)
print(res)
