def find_pair(ar, sum, n):
    l, r = 0, n-1
    count = 0
    ar.sort()
    while l < r:
        if ar[l] + ar[r] == sum:
            count += 1
            l += 1
            r -= 1
        elif ar[l] + ar[r] > sum:
            r -= 1
        elif ar[l] + ar[r] < sum:
            l += 1
        else:
            return -1
    return count


ar = list(map(int, input("Enter your array:\t").split(" ")))
sum = int(input("enter sum:\t"))
n = len(ar)
result = find_pair(ar, sum, n)
print("total pairs found", result)
