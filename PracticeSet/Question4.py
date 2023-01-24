def div(a,b):
    try:
        c = a/b
        print(f"{a} divide by {b} is {c}")
    except:
        print("Infinite")

if __name__=='__main__':
    x=int(input('Enter your no. : '))
    y=int(input("Enter your no. : "))
    div(x,y)