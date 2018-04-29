def first_occurance(ar, low, high, x):
    ar.sort()
    if high >= low:
        mid = (high+low)//2
        if x == ar[mid]:
            if mid == 0 or ar[mid-1] < x:
                return mid
            else:
                return first_occurance(ar, low, mid-1, x)
        elif x < ar[mid]:
            return first_occurance(ar, low, mid-1, x)
        else:
            return first_occurance(ar, mid+1, high, x)
    return -1


def last_occurance(ar, low, high, x):
    if high >= low:
        mid = (high + low)//2
        if x == ar[mid]:
            if ar[mid+1] > x or mid == high:
                return mid
            else:
                return last_occurance(ar, mid+1, high, x)
        elif x > ar[mid]:
            return last_occurance(ar, mid+1, high, x)
        else:
            return last_occurance(ar, low, mid-1, x)
    return -1


ar = list(map(int, input("Enter your array:\t").split(" ")))
n = len(ar)
x = int(input("Enter number to be found: \t"))
i = first_occurance(ar, 0, n-1, x)
j = last_occurance(ar, 0, n-1, x)
print("Number occurred\t", (j-i+1), "times")
