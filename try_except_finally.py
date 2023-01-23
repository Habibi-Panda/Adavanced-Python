try:
    a = int(input("Enter a number : "))
    c = 1/a
    print(c)

except Exception as e:
    print(e)
    exit()
#yaha kuch bhi ho jaye par finally hamesha excute hoga chahe
# try run ho ya exception aaye finally excute hoga hi
finally:
    print("We were done")

print("Thanks for using the program")