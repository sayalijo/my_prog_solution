# Using loop
def reverse_string(s):
    rev_str = ""
    for i in s:
        rev_str = i + rev_str
    return rev_str


s = input("enter your string: \t")
result = reverse_string(s)
print("Reversed string is:\t", result)
