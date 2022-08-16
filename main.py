import os
import shutil

from_dir = "C:/Users/namra/Downloads/Source"
to_dir = "C:/Users/namra/Downloads/Destination"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for i in list_of_files:
    name, extension = os.path.splitext(i)
    print(name)
    print(extension)
    if extension == "":
        continue
    if extension in [".png",".jpg",".gif", ".jpeg"]:
        path1 = from_dir + "/"  + i
        path2 = to_dir + "/" + "image files"
        path3 = to_dir + "/" + "image files " + i
        if os.path.exists(path2):
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            shutil.move(path1, path3)