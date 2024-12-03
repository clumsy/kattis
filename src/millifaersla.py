m, f, d = (int(input()) for _ in range(3))
res = "Monnei" if m < f and m < d else "Fjee" if f < m and f < d else "Dolladollabilljoll"
print(res)
