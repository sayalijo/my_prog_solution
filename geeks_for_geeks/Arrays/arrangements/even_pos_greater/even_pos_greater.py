def arrange(ar):
    ar.sort()
    n = len(ar)
    q = n -1
    p = 0
    arr = [0]*n
    for i in range(n):
        if (i+1) % 2 == 0:
            arr[i] = ar[q]
            q -= 1
        else:
            arr[i] = ar[p]
            p += 1
    return arr


ar = list(map(int, input("enter array:\t").split(" ")))
result = arrange(ar)
print(" ".join(map(str, result)))

