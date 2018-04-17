def linear_search(arr, x):
	for i in range(len(arr)):
		if arr[i] == x:
			return i
	return -1


x = int(input().strip())
arr = list(map(int, input().split(" ")))
result = linear_search(arr,x)
print("Element found at position:", result)
