while(True):
    print("press q to quit")
    a = input("Enter your value :")
    if a == 'q':
        break
    try:
        print("Tring......")
        a = int(a)
        if (a>6):
            print("you entered a number greater than 6")
    except Exception as e:
        print(f"Your input resulted in an error: {e}")

print("Thanks for playing this game")