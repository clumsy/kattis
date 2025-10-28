n, a = int(input()), (int(i) for i in input().split())
res = [1, *(i + 2 for i, _ in sorted(enumerate(a), key=lambda x: x[1]))]
print(*res)
