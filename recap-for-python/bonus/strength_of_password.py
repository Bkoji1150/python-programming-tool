
password = input("Enter new password: ")

result = {}
digit = False
uppercase = False

if len(password) >= 8:
    result['Length'] = True
else:
    result['Length'] = False

for i in password:
    if i.isdigit():
       digit = True
result['digit'] = digit

for i in password:
    if i.isupper():
        uppercase = True

result['Upper-case'] = uppercase

if all(result.values()):
    print(f"Strong password.")

else:
    print("Weak password")