n = int(input())
res = (
    f"{45 * n} ml gin\n"
    f"{30 * n} ml fresh lemon juice\n"
    f"{10 * n} ml simple syrup\n"
    f"{n} slice{'s' if n > 1 else ''} of lemon"
)
print(res)
