
password = input("Enter password: ")
count = 1

while password != "pass123":
    print(f"Sorry, user login failed!, logging {count} number of times")
    password = input("Enter password: ")
    count += 1

print("login successful")