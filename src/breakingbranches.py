n = int(input())
res = ["Alice", "1"] if n & 1 == 0 else ["Bob"]
print(*res, sep="\n")
