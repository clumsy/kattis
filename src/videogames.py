gms = {
    "fishing": "alice",
    "golf": "bob",
    "hockey": "charlie",
}
n = int(input())
for _ in range(n):
    s = input().split()
    if s[0] == gms[s[-1]]:
        res = f"{s[0]} already has {s[-1]}"
    else:
        res = f"{s[0]} borrows {s[-1]} from {gms[s[-1]]}"
        gms[s[-1]] = s[0]
    print(res)
