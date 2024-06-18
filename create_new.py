import shutil
import os

def copy_file_with_new_name(new_file):
    # Get the directory of the original file
    original_file = "other/leetcodeTemplate.py"
    directory = os.path.dirname(original_file)
    
    # Form the full path for the new file
    new_file_path = os.path.join(directory, new_file)
    
    # Copy the file
    shutil.copy(original_file, new_file_path)
    print(f"File copied from {original_file} to {new_file_path}")

# Example usage
new_file = input("new filename: ")


copy_file_with_new_name(new_file)

