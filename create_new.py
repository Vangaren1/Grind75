import shutil
import os

def copy_file_with_new_name(new_file):
    # Get the directory of the original file
    original_file = "other/leetcodeTemplate.py"
    directory = os.path.dirname(original_file)

    newDirectory = os.path.dirname("create_new.py")
    
    # Form the full path for the new file
    new_file_path = os.path.join(newDirectory, new_file)
    
    # Copy the file
    shutil.copy(original_file, new_file_path)
    print(f"File copied from {original_file} to {new_file_path}")

# Example usage
new_file = input("new filename: ")

if new_file[-3:] != '.py':
    new_file += ".py"


copy_file_with_new_name(new_file)

