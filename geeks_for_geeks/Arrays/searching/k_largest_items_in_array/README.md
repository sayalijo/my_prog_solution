https://www.geeksforgeeks.org/k-largestor-smallest-elements-in-an-array/

1) Sort the elements in descending order in O(nLogn)
2) Print the first k numbers of the sorted array O(k).



K largest elements from arr[0..n-1]

1) Store the first k elements in a temporary array temp[0..k-1].
2) Find the smallest element in temp[], let the smallest element be min.
3) For each element x in arr[k] to arr[n-1]
If x is greater than the min then remove min from temp[] and insert x.
4) Print final k elements of temp[]

Time Complexity: O((n-k)*k). If we want the output sorted then O((n-k)*k + klogk)
