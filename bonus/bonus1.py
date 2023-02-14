
contents = ["All carrots are to be sliced logitudinally",
            "The carrots were reportedly sliced.",
            "The slicing process was well processed"]

filenames = ["doc.txt","report.txt","presentation.txt"]

for content, filename in zip(contents, filenames):
    with open("files/{}".format(filename), "w") as file:
        file.write(content)
