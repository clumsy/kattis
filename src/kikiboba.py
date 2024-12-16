s = input()
k = b = 0
for c in s:
    k += c == "k"
    b += c == "b"
res = "boki" if k == b and b > 0 else \
      "kiki" if k > b else \
      "boba" if b > k else "none"
print(res)
