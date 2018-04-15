# Enter your code here. Read input from STDIN. Print output to STDOUT


def findcharges(n,k,arr,m):
    share = (sum(arr) - arr[k])//2
    if m == share:
        return "Bon Appetit"
    else:
        return (m - share)

n,k = input().split(" ")
n,k = [int(n), int(k)]
arr = [int(i) for i in input().split(" ")]
m = int(input())
result = findcharges(n,k,arr,m)
print(result)



