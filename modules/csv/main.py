import csv

with open("file/weather.csv") as file:
    data = list(csv.reader(file))

for row in data[1:]:
    print(row[0])