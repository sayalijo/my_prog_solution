def k_largest(arr,k):
    arr.sort(reverse=True)
    for i in range(k):
        print(arr[i], end=" ")


arr = list(map(int, input("Enter array:\t").split(" ")))
k = int(input("Enter k \t"))
k_largest(arr,k)
