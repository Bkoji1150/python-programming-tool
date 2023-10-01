
import glob

myfiles = glob.glob("../file/*.txt")

for filepath in myfiles:
    with open(filepath) as file:
        data = file.read()

print(data)