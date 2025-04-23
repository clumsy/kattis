from itertools import accumulate


mnth = list(accumulate([0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]))
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
d, m = (int(i) for i in input().split())
res = days[(mnth[m - 1] + d - 1 + 3) % 7]
print(res)
