import csv

path = "https://docs.google.com/spreadsheets/d/1_n6514Gt2oXjO4B6ysU2Xi6T1jsIwOcTbT3-p3eAlh0/edit#gid=1240919429"

with open(path) as file:
    data = list(csv.reader(file))

for row in data[1:]:
    print(row[0],row[1], row[2])