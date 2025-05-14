n = int(input())
for _ in range(n):
    s = input()
    need = set(chr(ord("a") + i) for i in range(26))
    missing = need - set(s.lower())
    res = "missing " + "".join(sorted(missing)) if missing else "pangram"
    print(res)
