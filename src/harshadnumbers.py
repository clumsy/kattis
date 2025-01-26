n = int(input())
res = n
while res % sum(int(d) for d in str(res)) != 0:
    res += 1
print(res)
