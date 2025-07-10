while True:
    try:
        s = input().split()
        names, nums = [], []
        for c in s:
            try:
                nums.append(float(c))
            except Exception:
                names.append(c)
        res = " ".join([str(sum(nums) / len(nums)), *names])
        print(res)
    except Exception:
        break
