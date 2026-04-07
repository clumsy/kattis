res = input()
while len(res) > 1:
    res = str(sum(int(c) for c in res))
print(res)
