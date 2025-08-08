import sys

lens = []
for line in sys.stdin:
    lens.append(len(line))
ma = max(lens)
res = sum((ma - s) ** 2 for s in lens[:-1])
print(res)
