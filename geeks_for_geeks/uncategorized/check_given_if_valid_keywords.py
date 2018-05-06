# a keyword is a “reserved word” by the language which convey a special meaning # to the interpreter.
# inbuilt module “keyword”
import keyword as k

s = 'sayali'
s1 = 'lambda'

print("Is string {} a valid keyword? - {} ".format('s',k.iskeyword(s)))
print("Is string {} a valid keyword? - {} ".format('s1', k.iskeyword(s1)))
print("Total keywords in python are: {}".format(len(k.kwlist)))
print("Keywaords are:",", ".join(k.kwlist))
