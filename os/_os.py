import os

# Create a directory
directory_name = "new_directory"
os.mkdir(directory_name)
print(f"Directory '{directory_name}' created.")

# Get current working directory
current_dir = os.getcwd()
print(f"The current dir is: {current_dir}")

# Get list of files and directories in current directory
files_and_dirs = os.listdir()
print(f"All files and dirs: {files_and_dirs}")

# Renaming a file/directory
old_name = "sample.txt"
new_name = "to_be_deleted.txt"
os.rename(old_name,new_name)
print(f"{old_name} renamed to {new_name}.")

# Removing a file or directory
file_to_remove = "to_be_deleted.txt"
dir_to_remove = "new_directory"
os.remove(file_to_remove)
os.remove(dir_to_remove)
print(f"{file_or_dir_name} and {dir_to_remove} removed.")

# Change the current working directory
new_dir = "new_directory"
os.chdir(new_dir)
print(f"Current working directory changed to {new_dir}.")

# Get environment variables
env_var = os.environ
for variable, value in env_var.items():
    print(f"{variable}: {value}")
