n = int(input())
a, b, c = 1, 0, 0
for _ in range(n + 1):
    res = a + b + c
    a, b, c = b, c, res
print(res)

# n = int(input())
# dp = [0] * (n + 1)
# dp[0] = 1
# for i in range(n):
#     dp[i + 1] = dp[i - 2] + dp[i - 1] + dp[i]
# res = dp[-1]
# print(res)
