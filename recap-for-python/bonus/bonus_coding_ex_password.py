"""
Coding Exercise 2
Write a program that:

1. asks users to enter a password.

2. returns "Great password there" if the password has more than 7 characters.

3. returns "Password is OK, but not too strong" if the password has exactly 7 characters.

4. returns "Your password is weak" if the password has 7 or fewer characters.

"""
password = input("Enter a password: ")

if len(password) > 7:
    print("Great password there")
elif len(password) == 7:
    print("Password is OK, but not too strong")
elif len(password) < 7:
    print("Your password is weak")
