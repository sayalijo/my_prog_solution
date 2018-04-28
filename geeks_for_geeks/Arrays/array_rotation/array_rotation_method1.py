def rotate_array(arr,n,d):
    temp = arr[:d]
    arr = arr[d:]
    for each in temp:
        arr.append(each)
    return arr
	



n = int(input("Please enter array size \t"))
arr = list(map(int, input("Please enter array elements \t").split(" ")))
d = int(input("Please enter array to be rotated by\t"))
result = rotate_array(arr, n, d)
print(result)
