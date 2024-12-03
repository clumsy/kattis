t, k = (int(input()) for _ in range(2))
res = "MAGA!" if t > k else "FAKE NEWS!" if t < k else "WORLD WAR 3!"
print(res)
