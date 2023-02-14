
date = input("Enter today's data: ")
mood = input("How do you rate your mood for today on a scale of 1 - 10?: ")
journal = input("Let your thought flow:\n")

with open(f"files/journal/{date}.text", "w") as file:
    file.write(mood)
    file.write(journal)
