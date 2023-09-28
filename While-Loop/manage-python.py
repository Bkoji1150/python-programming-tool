
password = input("Enter password: ")
count = 1

while password != "pass123":
    print(f"wrong password, try again...")
    password = input("Enter password: ")
    count += 1
    if count ==3:
        break


print("login successful")