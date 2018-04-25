from itertools import combinations
N = int(input())
arr = input().split(" ")
K = int(input())

combination_list = list(combinations(arr,K))
l = [1 for each in combination_list if 'a' in each]
print(len(l)/len(combination_list))


