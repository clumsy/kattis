n = int(input())
cs = {}
for k, v in  {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}.items():
    for c in v:
        cs[c] = str(k)
ws = [input() for _ in range(n)]
s = input()
res = sum("".join(cs[c] for c in w) == s for w in ws)
print(res)
