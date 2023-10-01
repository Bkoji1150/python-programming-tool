
feet_inches = input("Enter feet and inches: ")


def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


parse = parse(feet_inches)
result = convert(parse['feet'], parse['inches'])

print(f"{parse['feet']} feet and {parse['inches']} is equal to {result}Meters")
if result < 1:
    print("The kid is too small")
else:
    print("Kid can use the slide.")