https://www.geeksforgeeks.org/binary-search/

Given a sorted array arr[] of n elements, write a function to search a given element x in arr[].

The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(Log n).

1. Compare x with the middle element.
2. If x matches with middle element, we return the mid index.
3. Else If x is greater than the mid element, then x can only lie in right half subarray after the mid element. So we recur for right half.
4. Else (x is smaller) recur for the left half.
