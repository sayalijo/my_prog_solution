def missing_element(arr):
    x1 = 1
    x2 = 1
    n = len(arr)
    for i in range(n):
        x1 ^= arr[i]
    for i in range(n+2):
        x2 ^= i
    print(x1, x2) 
    return x1^x2


arr = list(map(int, input("enter your array").split(" ")))
result = missing_element(arr)
print("Your missing element is array is", result)
