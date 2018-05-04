def minimum_swap(ar, k):
    l,r, count = 0,len(ar)-1,0    
    while l < r:
        while ar[l] <= k:
            l += 1
        print(l)
        while ar[r] >k:
            r -= 1
        ar[l], ar[r] = ar[r], ar[l]
        count += 1
        l += 1
        r -= 1
    return count


ar = list(map(int, input("Enter your array:\t").split(" ")))
k = int(input("Enter k:\t"))
result = minimum_swap(ar, k)
print("MInimum swaps required: {}".format(result))
