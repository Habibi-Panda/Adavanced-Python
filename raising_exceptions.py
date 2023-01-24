# try:
#     a = int(input("Enter your value : "))
#     c = 1/a
#     print(c)
# except :
#     raise ValueError("Please enter correct value")


def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not good - panda")
# here i use (if __name__ == '__main__':) this because if
# i need to run increment() funtion any other file 
# there no need to run a or n variable
if __name__ == '__main__':
    # print(__name__)
    n = input('Enter your value : ')
    a = increment(n)
    print(a)