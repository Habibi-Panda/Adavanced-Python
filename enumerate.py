list1 = ["Panda","Hello",45,56,340]
# index = 0
# for item in list1:
#   print (item, index)
#   index += 1

for index, item in enumerate(list1):
    # The enumerate function adds counter to an iterable and returns it
    print(item, index ) #print the items of list1 with index
