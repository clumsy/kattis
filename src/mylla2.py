g = [input() for _ in range(3)]
won = any(g[i] == "OOO" or "".join(g[j][i] for j in range(3)) == "OOO" for i in range(3)) or \
      "".join(g[i][i] for i in range(3)) == "OOO" or \
      "".join(g[i][2 - i] for i in range(3)) == "OOO"
res = "Jebb" if won else "Neibb"
print(res)
