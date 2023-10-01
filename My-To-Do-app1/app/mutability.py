
filenames = ["1.RWA Data.txt", "2.Report.txt", "3.Presentations.txt"]

## Replace the "." with a dash
list_files = []
for filename in filenames:
    filename = filename.replace('.','-', 1)
    print(filename)