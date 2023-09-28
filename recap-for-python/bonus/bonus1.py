
filenames = ["1.Raw", "2.Report"]

filenames = [filename.replace(".","-") + "txt" for filename in filenames]
print(filenames)
