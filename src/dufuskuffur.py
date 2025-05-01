n, m = (int(input()) for _ in range(2))
res = "Dufur passa" if n < m else "Dufur passa ekki" if n > m else "Dufur passa fullkomlega"
print(res)
