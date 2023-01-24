def tab():
    num = int(input("Enter your number : "))
    table = [num*i for i in range(1,11)]
    print(table)

if __name__=='__main__':
    tab()