a = 50 #Global variable
def fun1():
    global a #pointing a like c programming
    print(f"Statement 1: The value of a is {a}") #50
    a = 10 #Local Variable
    print(f"Statement 2:The value of a is {a}") #10

fun1()
print(f"Statement 3:The value of a is {a}") #10
