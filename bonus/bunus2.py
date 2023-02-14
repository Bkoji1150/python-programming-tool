
filenames = ["1.docs", "1.report", "1.representation"]

filenames = [filename.replace(".", "-") + ".txt" for filename in filenames]
print(filenames)