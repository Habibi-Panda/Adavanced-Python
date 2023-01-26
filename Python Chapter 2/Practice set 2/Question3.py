# a = ["7","14","21","28","35","42","49","56","63","70"]
a = int(input("Enter your number : "))
b = [str(i*a) for i in range(1,11)]

list1 = "\n".join(b)
print("Table \n{}".format(list1))