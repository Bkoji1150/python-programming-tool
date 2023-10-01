
def calculate_age(year_of_birth, current_year=2023):
    age = current_year - year_of_birth
    return age

try:
    user_prompt = int(input("What is your year of birth?: "))
    age = calculate_age(user_prompt)
    print(f"Your current age is: {age} Years")
except ValueError:
    print("only date of the year is allowed. for example 2002")


