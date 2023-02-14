from getpass import getpass

password = getpass("Please enter password: ")

# IF PASSWORD LENGTH IS GREATER THAN 8
result = {}

if len(password) >= 8:
    result["Length"] = True
else:
    result["Length"] = False

# IF PASSWORD CONTAINS A DIGIT
digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digits"] = digit

# IF PASSWORD CONTAINS AN UPPERCASE CHARACTER
uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result["uppercase"] = uppercase

print(result)

if all(result.values()):
    print("Strong Password!")
else:
    print(f"Weak password because of ")

