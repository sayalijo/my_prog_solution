# Input  = {12, 34, 45, 9, 8, 90, 3}
# Output = {12, 34, 8, 90, 45, 9, 3} 
def rearrange(a):
    i,j = -1,0
    for j in range(len(a)):
        if (a[j]%2 == 0):
            i += 1
            a[i], a[j] = a[j], a[i]
    return a


ar = list(map(int, input("enter array\t").split(" ")))
result = rearrange(ar)
print("Your array is: \t" + " ".join(map(str, result)))


