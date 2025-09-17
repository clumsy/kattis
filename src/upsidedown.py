n, s = int(input()), input().split()
res = sorted((c[::-1] for c in s), reverse=True)
print(*res)
