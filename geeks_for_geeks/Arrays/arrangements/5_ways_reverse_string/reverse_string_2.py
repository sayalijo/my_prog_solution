# Using recursion
# popping out 1st char of string in each recursion and concatenating at end
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]


s = input("enter string: \t")
result = reverse_string(s)
print(result)


