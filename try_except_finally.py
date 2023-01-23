try:
    a = int(input("Enter a number : "))
    c = 1/a
    print(c)

except Exception as e:
    print(e)

finally:
    print("We were done")
