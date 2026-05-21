import os
import shutil

filesDir = input("Unorganized file directory: ")
outputDir = input("Output directory: ")

# Check if both directories exist
def directories_exist(files, output):
    if not os.path.exists(files) or not os.path.isdir(files):
        print("File directory does not exist!")
        return False
    elif not os.path.exists(output) or not os.path.isdir(output):
        print("Output directory does not exist!")
        return False
    else:
        return True

# Organize files by file type
def organize_files(files, output):
    with os.scandir(files) as entries:
        for entry in entries:
            if entry.is_file():
                sub_output = os.path.splitext(entry)[-1]
                entry_path = os.path.abspath(entry)
                output_path = output + "/" + sub_output

                # Create path if path does not exist
                os.makedirs(output_path, exist_ok = True)

                # Move file to output
                shutil.move(entry_path, output_path + "/" + entry.name)
            elif os.path.isdir(entry):
                entry_path = os.path.abspath(entry)
                output_path = output + "/folders"

                # Create path if path does not exist
                os.makedirs(output_path, exist_ok = True)

                # Move file to output
                shutil.move(entry_path, output_path + "/" + entry.name)

if directories_exist(filesDir, outputDir) == True:
    organize_files(filesDir, outputDir)
    print("Files successfully moved!")

# Prevent file from closing
input()