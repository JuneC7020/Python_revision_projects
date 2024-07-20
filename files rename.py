import os
import re

def rename_files(directory, pattern, new_pattern):
    # List all files in the directory
    files = os.listdir(directory)
    
    # Compile the regular expression pattern
    regex = re.compile(pattern)
    
    for filename in files:
        # Check if the file name matches the pattern
        if regex.match(filename):
            # Create a new name based on the new pattern
            new_name = re.sub(pattern, new_pattern, filename)
            
            # Create full file paths
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_name)
            
            # Rename the file
            os.rename(old_file, new_file)
            print(f'Renamed: {old_file} to {new_file}')

if __name__ == "__main__":
    directory = input("Enter the directory path: ")
    pattern = input("Enter the pattern to match (regex): ")
    new_pattern = input("Enter the new pattern to rename to: ")

    rename_files(directory, pattern, new_pattern)
    print("All matching files have been renamed.")
