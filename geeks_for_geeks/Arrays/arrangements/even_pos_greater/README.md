https://www.geeksforgeeks.org/rearrange-array-such-that-even-positioned-are-greater-than-odd/

Observe that array consists of [n/2] even positioned elements. If we assign largest [n/2] elements to the even positions and rest of the elements to the odd positions, our problem is solved. Because element at odd position will always be less than the element at even position as it is maximum element and vice versa. Sort the array and assign the first [n/2] elements at even positions.


ip: [ 1, 3, 2, 2, 5 ]
op: 1 5 2 3 2
