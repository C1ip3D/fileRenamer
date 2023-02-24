import os

source="oldfile.txt"
destination="newfile.txt"
os.rename(source,destination)
print("Source path renamed to destination path successfully")