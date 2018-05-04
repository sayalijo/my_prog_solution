def rearrange(a):
    i = -1
    for j in range(len(a)):
        if a[j] < 0:
            i += 1
            a[i], a[j] = a[j], a[i]
    
    l, r = 0, i+1
    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 2
        r += 1
    return a


a = list(map(int, input("Enter your array:\t").split(" ")))
result = rearrange(a)
print(" ".join(map(str, result)))
