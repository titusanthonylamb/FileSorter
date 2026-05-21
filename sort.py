import os
import platform
import shutil

filesDir = input("Unorganized file directory: ")
outputDir = input("Output directory: ")

def directories_exist(files, output):
    if not os.path.exists(files) or not os.path.isdir(files):
        print("File directory does not exist!")
        return False
    elif not os.path.exists(output) or not os.path.isdir(output):
        print("Output directory does not exist!")
        return False
    else:
        return True
    
def organize_files(files, output):
    with os.scandir(files) as entries:
        for entry in entries:
            if entry.is_file():
                print(entry.name)

if directories_exist(filesDir, outputDir) == True:
    organize_files(filesDir, outputDir)