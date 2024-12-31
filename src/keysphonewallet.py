n = int(input())
s = {input() for _ in range(n)}
res = ({"keys", "phone", "wallet"} - s) or ["ready"]
print(*res, sep="\n")
