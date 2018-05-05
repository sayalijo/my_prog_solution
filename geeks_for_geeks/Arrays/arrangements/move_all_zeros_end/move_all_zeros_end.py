# arr[]  = {1, 2, 0, 0, 0, 3, 6}
# Output : 1 2 3 6 0 0 0

def rearrange(ar):
    i,j = -1, 0
    for j in range(len(ar)):
        if ar[j] > 0:
            i += 1
            ar[i], ar[j] = ar[j], ar[i]
    return ar


array = list(map(int, input("Enter your array:\t").split(" ")))
result = rearrange(array)
print("Now your array is:\n", " ".join(map(str,result)))

