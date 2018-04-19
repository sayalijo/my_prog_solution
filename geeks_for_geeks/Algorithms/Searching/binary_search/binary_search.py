def binary_search(arr, x, start_index, end_index):
	if end_index >= 1:
		mid_index = start_index  + (end_index - start_index)//2
		if arr[mid_index] == x:
			return mid_index
		elif arr[mid_index] > x:
			return binary_search(arr, x,start_index,  mid_index - 1)
		else:
			return binary_search(arr, x, mid_index+1, end_index)
	else:
		return -1

x = int(input())
arr = list(map(int, input().split(" ")))
result = binary_search(arr, x, 0, len(arr)-1)
if result != -1:
	print("Element found at position", result)
else:
	print("Element not present in the given array")
