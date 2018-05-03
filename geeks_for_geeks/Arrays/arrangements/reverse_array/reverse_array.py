def reverse_array(ar):
    l,r = 0, len(ar)-1
    while l < r:
        ar[l],ar[r] = ar[r],ar[l]
        l += 1
        r -= 1
    return ar



ar = list(map(int, input("Enter array elements\t").split(" ")))
result = reverse_array(ar)
print("Reversed array is:\t", *result)
