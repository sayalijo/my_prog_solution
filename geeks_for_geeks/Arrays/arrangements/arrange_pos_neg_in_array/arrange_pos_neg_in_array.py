ar = list(map(int, input("Enter your array elements:\t").split(" ")))
neg_generator = (str(x) for x in ar if x < 0)
pos_generator = (str(x) for x in ar if x >= 0)
print(" ".join(neg_generator), end=" ")
print(" ".join(pos_generator))
