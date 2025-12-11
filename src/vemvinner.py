def check(g, v):
    return (
        any(all(g[r][c] == v for c in range(3)) for r in range(3))
        or any(all(g[r][c] == v for r in range(3)) for c in range(3))
        or g[0][0] == g[1][1] == g[2][2] == v
        or g[2][0] == g[1][1] == g[0][2] == v
    )


def winner(g):
    if check(g, "X"):
        return "Johan"
    if check(g, "O"):
        return "Abdullah"
    return "ingen"


g = [input().split() for _ in range(3)]
res = f"{winner(g)} har vunnit"
print(res)
