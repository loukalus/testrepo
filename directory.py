import os

path = "c:\\temp"
for root, dirs, files in os.walk(path):
    print("{0} has {1} files".format(root, len(files)))