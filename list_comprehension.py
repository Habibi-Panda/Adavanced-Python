#list comprehension is an elegant way to create based on existing lists
#Example 1
list1 = [2,3,4,5,6,7,8,9]
list2 = [i for i in list1 if i>6]
print(list2)

#Example 2
a = [2,3,14,54,23,43,10,24,89,78,98]
b = [i for i in a if i%2 == 0]
print(b)
