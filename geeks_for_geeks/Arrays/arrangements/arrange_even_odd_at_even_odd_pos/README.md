https://www.geeksforgeeks.org/even-numbers-even-index-odd-numbers-odd-index/

Input : arr[] = {3, 6, 12, 1, 5, 8}
Output : 6 3 12 1 8 5 

Input : arr[] = {10, 9, 7, 18, 13, 19, 4, 20, 21, 14}
Output : 10 9 18 7 20 19 4 13 14 21 


Approach :

Start from the left and keep two index one for even position and other for odd positions.
Traverse these index from left.
At even position there should be even number and at odd positions, there should be odd number.
Whenever there is mismatch , we swap the values at odd and even index.

