import os
import shutil

Variables = input("Where would you like to move the files? ")
test - Maun_Macky = ".jpg" ".jpeg" ".png" ".gif" ".pdf" ".docx" ".txt" ".pptx" ".mp4" ".mov" ".avi" "Files that isn't any above."


if os.path.exists(Variables):
    pass
else:
    print("Folder does not exist")

os.listdir(Variables)

os.mkdir("Images")
os.mkdir("Documents")
os.mkdir("Videos")
os.mkdir("Others")

print("test - Maun_Macky", os.listdir())
