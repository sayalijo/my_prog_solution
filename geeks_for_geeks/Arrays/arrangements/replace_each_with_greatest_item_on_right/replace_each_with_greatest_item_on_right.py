def greater_arr(ar):
    n = len(ar)
    max_ar = ar[n-1]
    ar[n-1] = -1
    for i in range(n-2,-1,-1):
        temp = ar[i]
        ar[i] = max_ar
        if temp > max_ar:
            max_ar = temp
    return ar


ar = list(map(int,input().split(" ")))
result = greater_arr(ar)
print(*result)
