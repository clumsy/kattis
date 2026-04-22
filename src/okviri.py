s = input()
n = len(s)
res = [None] * 5
res[0] = res[-1] = ".." + "...".join("#" if i % 3 != 2 else "*" for i in range(n)) + ".."
res[1] = res[-2] = "." + ".".join("#.#" if i % 3 != 2 else "*.*" for i in range(n)) + "."
res[2] = "".join(
    "."
    if i & 1 == 1
    else s[(i - 2) // 4]
    if (i - 2) % 4 == 0
    else "*"
    if res[1][i - 1] == "*" or (i < len(res[0]) - 1 and res[1][i + 1] == "*")
    else "#"
    for i in range(len(res[0]))
)
res = "\n".join(s for s in res)
print(res)
