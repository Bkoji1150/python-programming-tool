from getpass import getpass

password = getpass("Please enter password: ")

# IF PASSWORD LENGTH IS GREATER THAN 8
result = []
if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

# IF PASSWORD CONTAINS A DIGIT
digit = False
for i in password:
    if i.isdigit():
        digit = True

result.append(digit)

# IF PASSWORD CONTAINS AN UPPERCASE CHARACTER
uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result.append(uppercase)
if all(result):
    print("Strong Password!")
else:
    print("Weak password!")
