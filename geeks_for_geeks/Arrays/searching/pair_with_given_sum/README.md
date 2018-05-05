https://www.geeksforgeeks.org/write-a-c-program-that-given-a-set-a-of-n-numbers-and-another-number-x-determines-whether-or-not-there-exist-two-elements-in-s-whose-sum-is-exactly-x/



method 1: using sorting and l/r

hasArrayTwoCandidates (A[], ar_size, sum)
1) Sort the array in non-decreasing order.
2) Initialize two index variables to find the candidate 
   elements in the sorted array.
       (a) Initialize first to the leftmost index: l = 0
       (b) Initialize second  the rightmost index:  r = ar_size-1
3) Loop while l < r.
       (a) If (A[l] + A[r] == sum)  then return 1
       (b) Else if( A[l] + A[r] <  sum )  then l++
       (c) Else r--    
4) No candidates in whole array - return 0


METHOD 2 (Use Hashing)
This method works in O(n) time.

1) Initialize an empty hash table s.
2) Do following for each element A[i] in A[]
   (a)    If s[x - A[i]] is set then print the pair (A[i], x - A[i])
   (b)    Insert A[i] into s.

# Python program to find if there are
# two elements wtih given sum
 
# function to check for the given sum
# in the array
def printPairs(arr, arr_size, sum):
     
    # Create an empty hash set
    s = set()
     
    for i in range(0,arr_size):
        temp = sum-arr[i]
        if (temp>=0 and temp in s):
            print ("Pair with the given sum is", arr[i], "and", temp)
        s.add(arr[i])

