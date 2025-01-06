a = (int(input()) for _ in range(10))
res = len(set(i % 42 for i in a))
print(res)
