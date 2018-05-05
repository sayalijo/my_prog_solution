def arrange(ar):
    even, odd = 0, 1
    while even < len(ar) or odd < len(ar):
        while ar[even] % 2 == 0:
            even += 2
        while ar[odd] % 2 != 0:
            odd += 2
        ar[even], arr[odd] = ar[odd], ar[even]
        even += 2
        odd += 2
    return ar


arr = list(map(int, input("Enter array:\t").split(" ")))
result = arrange(arr)
print(" ".join(map(str, result)))


