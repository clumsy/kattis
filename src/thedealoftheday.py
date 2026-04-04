a = [int(i) for i in input().split()]
k = int(input())
res = 0
for i in range(1 << 10):
    if i.bit_count() == k:
        cur, j = 1, 0
        while (1 << j) <= i:
            if (1 << j) & i == (1 << j):
                cur *= a[j]
                if cur == 0:
                    break
            j += 1
        res += cur
print(res)
