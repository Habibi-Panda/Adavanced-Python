from functools import reduce

l = [4,2,3,55,5,1,-7,72]

val = reduce(max,l)
print(val)
