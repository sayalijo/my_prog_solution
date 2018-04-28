def get_median(arr1,arr2):
    n = len(arr1)
    if n == 0:
        return "Invalid arr"
    if n ==1:
        return (arr1[0] + arr2[0])//2
    if n == 2:
        return (max(arr1[0],arr2[0])+min(arr1[1],arr2[1]))//2
    m1 = median(arr1)
    m2 = median(arr2)
    # 1 2 3 4 5       7 8 9 10 11
    if m1 == m2:
        return m1
    if m1 <  m2:
        return get_median(arr1[n//2:],arr2[:n//2+1])
    if m1 > m2:
        return get_median(arr1[:n//2+1],arr2[n//2:])


def median(arr):
    n = len(arr)
    if n%2 != 0:
        return arr[(n//2)]
    else:
        return (arr[n//2] + arr[n//2 - 1])//2


arr1 = list(map(int, input("Enter first sorted array \t").split(" ")))
arr2 = list(map(int, input("Enter secord sorted array: \t").split(" ")))
result = get_median(arr1,arr2)
print("Median is", result)
