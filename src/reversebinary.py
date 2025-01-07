n = int(input())
res = int(bin(n)[2:][::-1].lstrip("0"), 2)
print(res)
