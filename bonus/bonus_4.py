
try:
    width = eval(input("Enter rectangle width: "))
    length = eval(input("Enter rectangle length: "))

    if width == length:
        exit("That looks like a square")

    area = width * length
    print(area)
except ValueError:
    print("Please enter a number.")