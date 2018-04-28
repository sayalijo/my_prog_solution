def k_largest(arr,k):
    temp = arr[:k]
    #min = min(temp)
    for each in arr[k:]:
        minimum = min(temp)
        if each > minimum:
            temp.append(each)
            temp.remove(minimum)
            #min = min(temp)
    print(*temp)






arr = list(map(int, input("Enter array elements: \t").split(" ")))
k = int(input("Enter k: \t"))
k_largest(arr,k)
