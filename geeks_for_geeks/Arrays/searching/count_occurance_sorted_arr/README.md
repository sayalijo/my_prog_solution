https://www.geeksforgeeks.org/count-number-of-occurrences-or-frequency-in-a-sorted-array/

Method 1: linear search and record count.

Method 2 (Use Binary Search)
1) Use Binary search to get index of the first occurrence of x in arr[]. Let the index of the first occurrence be i.
2) Use Binary search to get index of the last occurrence of x in arr[]. Let the index of the last occurrence be j.
3) Return (j – i + 1);
