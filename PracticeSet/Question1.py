def readFile(fileName):
    try:
        with open(fileName, "r") as f:
            print(f.read())
    except FileNotFoundError as d:
        print(f"File {fileName} is not found")

readFile("./PracticeSet/1.txt")
readFile("2.txt") #This file is not present that's why it show error
readFile("3.txt") #The file location is wrong that's why it show error